<template>
  <el-form :model="ArticleForm" ref="articleFormRef" :rules="rules" class="demo-form-inline">
    <el-form-item label="">
      <el-input v-model="ArticleForm.title" placeholder="请输入标题" style="width: 70%;margin-right: 12px;" />
      <el-button type="primary" @click="dialogVisible = true" style="margin-right: 12px;">发布</el-button>
      <el-dialog v-model="dialogVisible" title="发布文章" width="50%">
        <el-form-item label="文章标签">
          <el-tag v-for="tag in dynamicTags" :key="tag" class="mx-1" closable :disable-transitions="false"
            @close="handleClose(tag)">
            {{ tag }}
          </el-tag>
          <el-input v-if="inputVisible" ref="InputRef" v-model.trim="inputValue" class="ml-1 w-20" size="small"
            @keyup.enter="handleInputConfirm" @blur="handleInputConfirm" />
          <el-button v-else class="button-new-tag ml-1" size="small" @click="showInput">
            + New Tag
          </el-button>
        </el-form-item>


        <el-form-item label="添加封面">
          <el-upload class="avatar-uploader" action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload" :limit="1" list-type="picture">
            <img v-if="ArticleForm.imageUrl" :src="ArticleForm.imageUrl" class="avatar" />
            <el-icon v-else class="avatar-uploader-icon">
              <Plus />
            </el-icon>

          </el-upload>
        </el-form-item>
        <el-form-item label="文章摘要">
          <el-input v-model="ArticleForm.digest" type="textarea" rows="3" cols="20" style="resize: none;" />
        </el-form-item>

        <el-form-item label="文章类型">
          <el-radio-group v-model="ArticleForm.type">
            <el-radio label="originality">原创</el-radio>
            <el-radio label="reprint">转载</el-radio>
          </el-radio-group>
        </el-form-item>
        <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible = false">取消</el-button>
            <el-button type="primary" @click="">提交</el-button>
          </span>
        </template>
      </el-dialog>
      <el-button type="primary" @click="toDraft">保存为草稿</el-button>
    </el-form-item>
    <el-form-item>
      <Toolbar style="border-bottom: 1px solid #ccc;width:100%" :editor="editorRef" :defaultConfig="toolbarConfig"
        mode="default" />
      <Editor style="height: 500px;width:100%; overflow-y: hidden;" :v-model="ArticleForm.body"
        :defaultConfig="editorConfig" mode="default" @onCreated="handleCreated" />
    </el-form-item>
  </el-form>
</template>

<script setup lang="ts">
import '@wangeditor/editor/dist/css/style.css';

// 系统依赖
import { onBeforeUnmount, nextTick, ref, shallowRef, onMounted, reactive } from 'vue';

// element依赖
import type { FormInstance, FormRules, UploadProps, TagProps } from 'element-plus';
import { ElMessage, ElMessageBox, ElInput } from 'element-plus';
import { Plus } from '@element-plus/icons-vue'
const articleFormRef = ref<FormInstance>();

// wangeditor 依赖
import { Editor, Toolbar } from '@wangeditor/editor-for-vue';

// API 依赖
import { addArticleAPI } from "@/api/articles/index";

// 数据类型依赖
import { PublishArticleType, DraftArticleType, } from "@/api/articles/types";


// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
import { useAppStore } from "@/store/modules/app";
const userStore = useUserStore();
// const appStore = useAppStore();

// 初始化禁用
const dialogVisible = ref(false);


const ArticleForm = reactive({
  title: '', //标题
  body: '', //主体
  author: userStore.nickname, //作者
  imageUrl: '',  //封面
  tag: [] as Array<string>,   // 标签
  digest: '', //摘要
  type: 'originality',//文章类型：原创和转载
});

const rules = reactive<FormRules>({
  title: [
    { required: true, message: '标题不能空', trigger: 'change' },
  ],
  body: [
    { required: true, message: '内容不能空', trigger: 'change' },
  ],
  tag: [
    { required: true, message: '标签不能空', trigger: 'change' },
  ],
  digest: [
    { required: true, message: '标签不能空', trigger: 'change' },
  ],
});

// 编辑器实例，必须用 shallowRef
const editorRef = shallowRef();

// 内容 HTML
const valueHtml = ref('<p>hello</p>');

const toolbarConfig = {};
const editorConfig = { placeholder: '请输入内容...' };

const handleCreated = (editor: any) => {
  editorRef.value = editor // 记录 editor 实例，重要！
};


// 标签

var inputValue = ref('');
const dynamicTags = ArticleForm.tag;
const inputVisible = ref(false);
const InputRef = ref<InstanceType<typeof ElInput>>();

const handleClose = (tag: any) => {
  dynamicTags.splice(dynamicTags.indexOf(tag), 1)
};

const showInput = () => {
  inputVisible.value = true
  nextTick(() => {
    InputRef.value!.input!.focus()
  })
};

const handleInputConfirm = () => {
  if (inputValue.value) {
    dynamicTags.push(inputValue.value)
  }
  inputValue.value = '';
  inputVisible.value = false
};

// 封面
const handleAvatarSuccess: UploadProps['onSuccess'] = (
  response,
  uploadFile
) => {
  ArticleForm.imageUrl = URL.createObjectURL(uploadFile.raw!)
}

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  if (rawFile.type !== 'image/jpeg') {
    ElMessage.error('Avatar picture must be JPG format!')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error('Avatar picture size can not exceed 2MB!')
    return false
  }
  return true
}

// 保存为草稿
const toDraft = async () => {
  if (ArticleForm.title) {
    const DraftArticle: DraftArticleType = reactive({
      title: ArticleForm.title,
      body: ArticleForm.body,
      author: ArticleForm.author,
    });
    await addArticleAPI('313', DraftArticle, userStore.id)
      .then(() => {
        ElMessage.success("已保存为草稿");
      })
      .catch(() => {
        ElMessage.error("保存失败");
      })
  } else {
    ElMessage.error("标题不能空");
  }
};

const toPublish = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      ElMessage.success("文章已发布");
    } else {
      console.log('error submit!', fields);
    }
  })
};



// 模拟 ajax 异步获取内容
onMounted(() => {
  console.log(ArticleForm.type);
});

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
  const editor = editorRef.value;
  if (editor == null) return
  editor.destroy()
});

</script>
<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>
.avatar-uploader {
  position: relative;
  width: 160px;
  height: 90px;
  background-color: #f5f6f7;
  border-radius: 4px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
  border-bottom-left-radius: 4px;
  overflow: hidden;
  flex-shrink: 0;
  border: 1px dashed #15d;


}

.avatar-uploader .el-upload {
  height: 100%;
  width: 100%;
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.el-form-item {
  padding: 14px 0px 14px 0;
}

.el-textarea>textarea {
  resize: none;
}
</style>