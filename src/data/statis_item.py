#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mapst = {
    'action':{
        'type':{
            'store':'收藏',
            'dispic':'设置为无图模式',
            'ngmode':'设置为夜间模式',
            'follow':'跟帖',
            'reply':'回复跟帖',
            'support':'支持跟帖',
            'share':'跟帖分享',
            'ngr':'设置夜间无声推送',
            'lv':'点击直播',
            'chat':'点击聊天',
            'tfc':'点击头条浮层',
            'radio':'点击音频播放按钮',
            'cdr':'频道下拉刷新',
            'pnp':'频道上拉',
            'ckup':'点击推荐频道更新提示',
            'fnch':'点击财经频道大盘模块',
            'ckcw':'点击汽车频道web入口',
            'vdt':'点击体育直播间查看数据button',
            'msub':'点击自媒体频道我的订阅button',
            'fd':'点击自媒体频道发现button',
            'search':'搜索',
            'searchzmt':'自媒体订阅号搜索',
            'vsdksearch':'视频模块内容搜索',
            'adjp':'启动广告页跳转',
            'ad':'点击小羊广告',
            'atoast':'头条跳转弹窗出现',
            'ctoast':'头条跳转弹窗点击',
            'editch':'频道管理页面点击“编辑”按钮',
            'cpurl':'文章分享“复制链接”',
            'update':'应用内升级通知点击“确定”',
            'cache':'音视频内容缓存按钮（不包括fm）',
            'chmark':'“上次阅读到这里”',
            'keywd':'正文页TAG点击',
            'fmdload':'fm频道音频播放单页下载操作',
            'fmwin':'fm播放浮窗点击操作',
            'pushvio':'推送声音开/关操作',
            'dlresult':'离线下载成功/失败',
            'upscreen':'频道首页上拉',
            'btnnews':'屏幕底部位置一按钮点击',
            'btnmedia':'屏幕底部位置二按钮点击',
            'btnhot':'屏幕底部位置三按钮点击',
            'btnmy':'屏幕底部位置四按钮点击',
            'mmtag':'“美女”频道分类标签点击',
            'left':'“左划”切换频道',
            'right':'“右划”切换频道',
            'btnsub':'“订阅自媒体”',
            'btnrecmd':'“订阅算法频道”',
            'chsub':'频道订阅',
            'chunsub':'取消频道订阅',
            'aloc':'天气设置页“主动切换地域”',
            'ploc':'天气设置页“被动切换地域”',
            'suborder':'直播间预约按钮点击',
            'livecomt':'直播间用户评论',
            'vzoom':'直播间视频缩小功能点击',
            'readrecord':'底部位置四按钮界面中的“历史”点击',
            'bonus':'“金币任务”点击',
            'ugrade':'“用户等级”点击',
            'sign':'签到',
            'sharescreen':'截屏分享',
            'txtmark':'截屏分享“添加水印”',
            'picmark':'截屏分享“添加表情”',
            'popwin':'弹出引导提示',
            'pushtipok':'弹出地域切换引导提示',
            'swloc':'房产频道“位置切换”按钮点击',
            'swlocvct':'房产频道“位置切换”点击确定（切换成功）',
            'subquest':'问卷调查提交按钮点击',
            'clicktab':'推荐频道标签点击',
            'negative':'频道负反馈内容确认',
            'later':'升级弹框“以后再说”按钮点击',
            'upnow':'升级弹框“立即更新”按钮点击',
            'download':'凤凰视频推荐位“下载”点击',
            'opvideo':'凤凰视频推荐位“打开”点击',
            'rdislike':'内容“x”按钮点击',
            'welfare':'个人中心公益入口点击',
            'ckad':'中韩交流图片广告点击',
            'adjump':'开机广告跳过按钮点击',
            'inews':'【点击，查看要闻 】按钮点击',
            'closedan':'关闭弹幕按钮点击',
            'opendan':'显示弹幕按钮点击',
            'setdan':'弹幕设置区功能点击',
            'allorder':'点击预约卡片查看全部预约（非预约按钮）',
            'activity':'“我-活动”点击',
            'cpminfo':'由红包渠道引入的Android新用户首页弹窗曝光',
            'cpmclick':'由红包渠道引入的Android新用户首页弹窗点击',
            'hotsearch':'搜索页面热门搜索关键词点击',
            'addislike':'信息流广告负反馈按钮点击',
            'adclose':'正文广告关闭按钮点击',
            'pushup':'FM付费频道上推翻页操作',
            'buybutton':'FM确认购买按钮点击',
            'buyfailed':'FM购买失败原因',
            'nowpay':'FM-h5立即支付按钮点击',
            'floatad':'浮层广告点击',
            'hikevapp':'相关阅读列表拉起视频客户端的卡片点击',
            'mybuy':'我的已购',
            'myaccount':'我的账户',
            'gameclick':'用户中心游戏按钮点击',
            'financeclick':'用户中心理财按钮点击',
            'fmtool':'FM快捷条',
            'fmtry':'FM点击试听',
            'repeat':'视频重播按钮',
            'upvote':'点赞',
            'downvote':'点踩',
            'vsdkbtre':'视频模块评论按钮点击',
            'subpay':'自媒体商城购买按钮',
            'bspage':'点击定向推荐内容',
            'btnchk':'点击立即验证',
            'btnlogin':'绑定或登陆',
            'btnreg':'注册',
            'btnvc':'验证码点击',
            'btnlogin2':'继续登录',
            'setbdph':'个人中心设置手机号',
            'setpw':'个人中心设置密码',
            'setbdsns':'个人中心设置社交平台账号',
            'setsns_wx':'设置社交平台账号时打开/关闭微信开关',
            'setsns_qq':'设置社交平台账号时打开/关闭qq开关',
            'setsns_wb':'设置社交平台账号时打开/关闭微博开关',
            'exitbdp':'点击绑定页回退按钮',
            'btntop1':'Fm按钮',
            'btnlive':'直播按钮',
            'btnmymsg':'个人主页消息按钮',
            'cgloc':'切换定位',
            'lorder':'直播预约',
            'lunorder':'取消直播预约',
            'replymore':'评论页-更多回复',
            'replayclick':'评论页-点击某条评论',
            'prtscn':'截屏操作',
            'btnutopic':'用户兴趣选择',
            'popup_close':'标准弹窗-关闭按钮',
            'popup_click':'标准弹窗-点击',
            'cmdtiem_more':'兴趣item-查看更多',
            'fresh_new':'身边人',
            'rpack_tk_cdr':'任务红包_下拉',
            'rpack_tk_reply':'任务红包_评论',
            'rpack_tk_ts':'任务红包_分享',
            'rpack_tk_pop':'任务红包_弹窗',
            'rpack_tk_popbtn':'任务红包_弹窗_确认',
            'rpack_btndraw':'红包收入页-提现按钮',
            'rpack_hisaward':'福袋活动页-点击上期开奖',
            'rpack_sssq':'福袋开奖弹窗-晒晒手气',
            'rpack_zlyc':'福袋开奖弹窗-再来一次',
            'srh_delall':'搜索页-清空搜索历史',
            'src_del':'搜索页-叉号按钮点击',
            'newth_po':'发布动态',
            'share_newth':'转发到站内（分享到身边人）',
            'newth_shieldt':'身边人-屏蔽动态',
            'newth_shieldm':'身边人-屏蔽人',
            'newth_onlyme':'身边人-仅自己可见',
            'newth_delpo':'身边人-删除',
            'newth_sortf':'身边人-按距离排序',
            'newth_sortt':'身边人-按时间排序',
            'newth_sorth':'身边人-按热度排序',
            'set_noti':'常驻通知栏开关',
            'newth_tjhy_phb':'身边人添加好友-同步通讯录',
            'newth_ tjhy_msg':'身边人添加好友-短信通知',
            'srhmo_user':'搜索结果页_查看更多_用户',
            'srhmo_v':'搜索结果页_查看更多_视频',
            'srhmo_qa':'搜索结果页_查看更多_问问',
            'srhmo_pg':'搜索结果页_查看更多_网页结果',
            'zz_buy':'知之-立即购买',
            'zz_comment':'知之-我要评价',
            'fin_zx':'财经_自选按钮',
            'chsmg':'频道批量订阅',
            'chsunmg':'频道批量取消订阅',
            'srhmo_fm':'搜索结果页-FM',
            'srhmo_nov':'搜索结果页-小说',
            'srhmo_zz':'搜索结果页-知之',
            'pushtip_1':'推送引导提示',
            'pushtip_2':'推送引导提示',
            'pushtip_3':'推送引导提示',
            'pushtip_':'推送引导_开启',
            'vcp_no':'收不到验证码',
            'forget_password':'忘记密码',
            'vcv_ok':'语音验证码-现在接听',
            'vcv_close':'语音验证码-取消',
            'vcp_ok':'验证码-确认',
            'vcp_close':'验证码-取消',
            'zz_upplay':'播放器缩略图上方播放按钮的点击',
            'zz_bought':'已有购买id为xx',
            'zz_rfirst':'返回第一期再看一遍id为xx',
            'zz_next':'下一期点击id为xx',
            'fmpg_zz':'知之id为xx',
            'fmpg_story':'小说id为xx',
            'fmpg_FM':'FM的id为xx',
            'ng_slide5':'进入页面后第一条发一次曝光，之后下滑动每可见5条新内容发送一次',
            'update_new':'升级新版按钮点击',
            'attention':'去关注',
            'cgds_':'炒股大赛',
            'ensure':'确定',
            'abolish':'取消',
            'skip_comment':'流内点击评论打开正文页并定位到评论区',
            'push_back':'从推送文章中按back键返回',
            'fic_entrance':'虚拟行情入口',
            'me_cancel':'个人中心取消',
            'join_on':'加入登录',
            'pushopen':'打开推送',
            'nonet':'无网络',
            'binding':'绑定',
            'top_info':'头条流曝光',
            'top_off':'头条流关闭',
            'turnoff':'关闭',
            'deploy_docid':'展开全文',
            'back_lgp':'push落地页接入主板返回按钮',
            'qq_dl':'qq登录',
            'wx_dl':'微信登录',
            'weib_dl':'微博登录',
            'leftslip':'热点聚合页左滑',
            'hotsee_more':'热点聚合页查看更多',
            'hotsee_other':'查看其它热点',
            'srh_history':'搜索页_搜索历史点击',
            'srh_hot':'搜索页_热门标签',
            'srh_more':'搜索页_查看更多热点点击',
            'get_code':'获取验证码',
            'success_code':'成功获取验证码',
            'close_popup':'关闭弹窗',
            'btnbind':'登录页登录',
            'codetail_camera':'相机',
            'codetail_photo':'相册',
            'cddetail_cross':'叉号',
            'push_unseal':'去开启',
            'dl_click':'一键登录'
        }
    },
    'page':{
        'type':{
            'article':'文章',
            'sv':'小视频',
            'pic':'图集',
            'piclive':'图文直播间',
            'ch':'频道',
            'topic':'策划专题首页',
            'sportslive':'体育直播间',
            'video':'视频',
            'set':'设置',
            'comment':'评论',
            'ad':'广告',
            'other':'其它',
            'sub':'自媒体订阅',
            'ph':'个人主页',
            'fmpg':'fm频道',
            'vch':'视频下导航分类',
            'vlive':'视频直播间',
            'live':'直播主页,列表和栏目',
            'pgplay':'当页播放(视频或音频)',
            'sns_':'身边人sns',
            'zzplay':'知之播放',
            'newsgroup':'新闻24小时',
            'comment_inner':'二级评论',
            'comment_svideo':'短视频二级评论',
            'bubble':'泡泡秀',
            'login_dl':'注册登录弹框',
            'closepush_stay':'关闭推送挽留',
            'comment_detail':'评论详情',
            'h5':'H5'
        }
    },
    'duration':{
            'type':{
                'ch':'编辑频道首页',
                'sv':'小视频',
                'chrcmd':'算法频道首页',
                'article':'文章单页',
                'chvideo':'视频频道中的二级频道',
                'video':'视频',
                'pic':'图集'
            }
    },
    'v':{
        'yn':{
            'yes':'成功播放第一帧',
            'no':'播放第一帧失败'
        }
    },
    'in':{
        'type':{
            'direct':'直接打开',
            'push':'推送打开',
            'outside':'从第三方打开',
            'desktop':'由桌面组件打开',
            'dph':'升级推送打开',
            'msg':'私信推送打开',
            'notification':'常驻通知栏打开'
        },
        'status':{
            'on':'已登录',
            'off':'未登录'
        }
    },
    'pushaccess':{
        'pushtype':{
            'machine_cmt_reply':'评论回复push-机器自动推送',
            'machine_media_subscribe':'媒体订阅push-机器自动推送',
            'machine_interest':'机器兴趣push',
            'machine_weather_alarm':'天气预警push-机器自动推送',
            'editor_full':'编辑全量push',
            'editor_interest':'编辑兴趣push',
            'editor_loc':'编辑地域push',
            'editor_trace':'编辑追踪push'
        }
    },
    'openpush':{
        'type':{
            'n':'从推送列表中',
            'o':'在app运行中'
        },
        'pushtype':{
            'machine_cmt_reply':'评论回复push-机器自动推送',
            'machine_media_subscribe':'媒体订阅push-机器自动推送',
            'machine_interest':'机器兴趣push',
            'machine_weather_alarm':'天气预警push-机器自动推送',
            'editor_full':'编辑全量push',
            'editor_interest':'编辑兴趣push',
            'editor_loc':'编辑地域push',
            'editor_trace':'编辑追踪push'
        }
    },
    'ts':{
        'type':{
            'article':'文章',
            'pic':'图集',
            'piclive':'图文直播间',
            'ch':'频道',
            'topic':'策划专题首页',
            'sportslive':'体育直播间',
            'video':'视频',
            'set':'设置',
            'comment':'评论',
            'ad':'广告',
            'other':'其它',
            'sub':'自媒体订阅',
            'ph':'个人主页',
            'fmpg':'fm频道',
            'vch':'视频下导航分类',
            'vlice':'视频直播间',
            'live':'直播主页,列表和栏目',
            'pgplay':'当页播放(视频或音频)',
            'sns_':'身边人sns',
            'zzplay':'知之播放',
            'newsgroup':'新闻24小时',
            'comment_inner':'二级评论',
            'comment_svideo':'短视频二级评论',
            'bubble':'泡泡秀',
            'login_dl':'注册登录弹框',
            'closepush_stay':'关闭推送挽留',
            'comment_detail':'评论详情'
        }
    },
    'end':{
        'status':{
            'back':'back键退出',
            'home':'home键退出'
        }
    },
    'desktop':{
        'op':{
            'add':'使用桌面组件',
            'del':'删除桌面组件'
        }
    },
    'login':{
        'type':{
            'swb':'新浪微博',
            'twb':'腾讯微博',
            'ifeng':'凤凰通行证',
            'qzone':'qq空间',
            'wct':'微信'
        }
    }
}

finduserkey = [
    '352049073522022',
    '866932035508313',
    '9109cf4d98a40067',
    'b16ed6152eaf0f5ed0a0f9e092f24adda6922d9f',
    '358374067863099',
    '866479022917412',
    '868773029096560',
    '866013034861613',
    '358520088907147',
    '862005035801790',
    '862006035014634',
    '351615081079410',
    '38474ac14347011c',
    '868144030038191',
    '3ac8bbf766884f2ea2736998e5748d12'
]


print(mapst.get('action').get('type').get('fhjkds'))






# userkey:4362743782832891738921

# action
# 2018-10-28+09:54:59, 执行了(type)操作.

# page
# 2018-10-28+09:54:59, 进入了(type)(id)页面.

# duration
# 2018-10-28+09:54:59, 在(type)停留(sec)秒.

# v
# 2018-10-28+09:54:59, 在(ref),播放视频(pdur)秒,(yn)

# adclick
# 2018-10-28+09:54:59, 点击广告.

# in
# 2018-10-28+09:54:59, (type)客户端,用户状态:(status)

# pushaccess
# 2018-10-28+09:54:59, 收到推送,推送类型:(pushtype),推送通道:(ref)

# openpush
# 2018-10-28+09:54:59, (type)打开推送,推送类型:(pushtype),推送通道:(ref)

# ts
# 2018-10-28+09:54:59, 在(ch)频道,(type)页面,进行了分享操作.

# end
# 2018-10-28+09:54:59, (status)客户端,此次客户端运行时长(odur)秒

# desktop
# 2018-10-28+09:54:59, (op)

# login
# 2018-10-28+09:54:59, 用户用(type)登录客户端.

# except
# 2018-10-28+09:54:59, 客户端异常退出.





