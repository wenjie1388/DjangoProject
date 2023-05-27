import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { PublishArticleType , DraftArticleType,NavArticlesType,HotNewsType,ArticleReadingType,ArticleGuide6Type} from './types';

/**
 * 获取文章主体内容 
 * @param path_id  03010104:获取阅读类型的文章;03010501:用户点赞;03010502:用户收藏
 * @returns NavArticlesType
 */
export function getArticleAPI(vId:string,pathId: string|string[]){
  return request({
    url: '/'+vId+'/articles/'+pathId,
    method: 'get',
  });
}


/**
 * 点赞和收藏动作
 * @param path_id  03010501:用户点赞;03010502:用户收藏
 * @returns 
 */
export function addUpvoteCollectAPI(vId: string, pathId: string | string[], articleId: string|string[]){
  return request({
    url: '/'+vId+'/articles/'+pathId+'/'+articleId,
    method: 'get',
  });
}


/**
 * 获取评论
 * @param articleId 
 * @returns 
 */
export function getCommentsApi(vId:string,articleId:string | string []){
  return request({
    url: '/'+vId+'/comments/'+articleId,
    method: 'get',
  });
};



/**
 * 添加一级评论
 * @param articleId 
 * @param commentForm 评论表单
 * @returns 
 */
export function addComment1Api(vId:string,articleId:string | string [],commentForm:object){
  return request({
    url: '/'+vId+'/comments/'+articleId,
    method: 'post',
    data:commentForm,
  });
};
/**
 * 添加二级评论
 * @param articleId 
 * @param commentForm 评论表单
 * @returns 
 */
export function addComment2Api(vId:string,articleId:string | string [],comment1:string,commentForm:object){
  return request({
    url: '/'+vId+'/comments/'+articleId+'/'+comment1,
    method: 'post',
    data:commentForm,
  });
};
/**
 * 删除评论
 * @param articleId 
 * @param commentId 
 * @returns 
 */
export function deleteCommentApi(articleId: string | string[], commentId: string) {
  return request({
    url: '/v1/articles/'+articleId+'/'+commentId,
    method: 'delete',
  });
};



//=========================================



















/**
 * 新增草稿或发布文章
 * @param key '312':发布；'313':草稿
 * @param articleForm 文章表单
 * @param uid 用户id
 * @returns 
 */
export function addArticleAPI(key:string,articleForm:PublishArticleType|DraftArticleType,uid:string): AxiosPromise {
  return request({
    url: '/v1/article/'+key+"/"+uid,
    method: 'post',
    data:articleForm,
  });
}

/**
 * 获取推荐文章
 * @param key 03010101:推荐文章  03010102:热榜文章
 * @returns NavArticlesType
 */
export function ArticlesAPI(key:string): AxiosPromise<NavArticlesType>{
  return request({
    url: '/v1/articles/'+key,
    method: 'get',
  });
}

/**
 * 获取热点新闻
 * @returns 
 */
export function HotNewsAPI(): AxiosPromise<HotNewsType>{
  return request({
    url: '/v1/articles/03010103',
    method: 'get',
  });
};





/**
 * 获取指定的文章
 * @param path_id  03010104:获取阅读类型的文章
 * @returns NavArticlesType
 */
export function searchArticlesAPI(query:object ,): AxiosPromise<ArticleReadingType>{
  return request({
    url: '/v1/articles',
    method: 'get',
    params:query,
  });
}


/**
 * 获取文章阅读内容
 * @param Article_id 
 * @returns 
 */
export function ArticleReadingAPI(Article_id:string | string []): AxiosPromise<ArticleReadingType>{
  return request({
    url: '/v1/articles/03010104',
    method: 'get',
    params:{'id':Article_id}
  });
};

/**
 * 文章导读6
 * @param uid 用户ID|
 * @returns 
 */
export function ArticleGuide6API(uid:string | string []): AxiosPromise<ArticleGuide6Type>{
  return request({
    url: '/v1/articles/03010105/'+uid,
    method: 'get',
  });
};

