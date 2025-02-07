from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Plain
import re

@register("qq_official_url_cleaner", "ave_mujica-saki", "为QQ官方API修改发送消息的链接，以防止消息被屏蔽", "1.0.0", "https://github.com/AstrBot-Devs/qq_official_url_cleaner")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.on_decorating_result()
    async def helloworld(self, event: AstrMessageEvent):
        '''为QQ官方API屏蔽发送消息的链接，以防止消息被屏蔽''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        result = event.get_result()
        new_chain = []
        for message in result.chain:
            if isinstance(message, Plain):
                message.text = re.sub(r'https?://[^\s\u4e00-\u9fa5\p{P}()]]+', '[被屏蔽的链接]', message.text)
                message.text = message.text.replace('.', ' . ')
                new_chain.append(message)
            else:
                new_chain.append(message)
        result.chain = new_chain
