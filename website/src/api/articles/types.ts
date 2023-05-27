

/**
 * 发布文章的参数
 */
export interface PublishArticleType {
    author: string;
    body: string;
    cover: string;
    tag: string;
    title: string;
    type: string;
}


/**
 * 草稿文章的参数
 */
export interface DraftArticleType {
    title: string;
    body: string;
    author: string;
}


/**
 * 推荐文章
 */
export interface NavArticlesType {
    /**
     * id
     */
    id: string;
    /**
     * 作者
     */
    author: string;
    /**
     * 摘要
     */
    digest: string;
    /**
     * 封面
     */
    imgUrl: string;
    /**
     * 标题
     */
    title: string;
    /**
     * 点赞量
     */
    upvote: string;
}

/**
 * 热点新闻
 */
export interface HotNewsType {
    id: string;
    digest: string;
    titl: string;
}

/**
 * @param 文章阅读
 */
export interface ArticleReadingType {
    body: string;
    collect: number;
    create_date: string;
    id: string;
    /**
     * 阅读量
     */
    pageviews: number;
    subfield1: string[];
    tags: string[];
    title: string;
    uid: string;
    /**
     * 点赞量
     */
    upvote: number;
}






/**
 * @param 文章导读8
 */
export interface ArticleGuide6Type {
    /**
     * 作者
     */
    author: string;
    /**
     * 收藏量
     */
    collect: number;
    /**
     * 摘要
     */
    digest: string;
    /**
     * id
     */
    id: string;
    /**
     * 封面
     */
    imgUrl: string;
    create_date: string;
    /**
     * 阅读量
     */
    pageviews: number;
    /**
     * 标题
     */
    title: string;
    /**
     * 点赞量
     */
    upvote: number;
}



/**
 * 评论1
 */
export interface Comment1Type {
    articleid: string;
    comment2: Comment2[string];
    date: string;
    fromu: string;
    id: string;
    message: string;
}

/**
 * 评论2
 */
export interface Comment2 {
    date: string;
    fromu: string;
    message: string;
    id: string;
}





