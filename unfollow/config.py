#!/usr/bin/evn python3

import toml
import os

from unfollow.unfollow import UNFOLLOW_PATH

default_config = """
[appearance]

[apperance.styling] # set the theme
theme = "regular"

[apperance.emojis]
init_emoji = ":dancer:"
fetch_success_emoji = ":heavy_check_mark:"
no_unfollows_emoji = ":raised_hands:"
follow_count_emoji = ":fire:"
thankyou_emoji = ":pray:"

[locale] # language
locale = "english"

# text for each language for each theme
[locale.english]
[locale.english.regular]
welcome_message = ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] Python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Fetched github followers"
no_unfollows_message = "[green]:raised_hands: [underline]No unfollows!"
end_message = ":fire: You have {follower_num} followers. Keep up the good work\\n"
thankyou_message = ":pray: Thanks for using this project"

[locale.english.panels]
welcome_message = ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] Python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Fetched github followers"
no_unfollows_message = "[white on #308012] No unfollows! [/white on #308012]                                "
end_message = ":fire: You have {follower_num} followers. Keep up the good work\\n"
thankyou_message = ":pray: Thanks for using this project"

[locale.english.bubbles]
welcome_message_a = "[white on purple]Welcome to[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]the Python implementation[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]by Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Fetched github followers[/white on cyan]"
no_unfollows_message = "[white on green4]No unfollows![/white on green4]"
end_message_a = "[white on purple]You have {follower_num} followers.[/white on purple]"
end_message_b = "[white on magenta]Keep up the good work![/white on magenta]"
thankyou_message = "[white on blue]Thanks for using this project[/white on blue]"


[locale.portuguese]
[locale.portuguese.regular]
welcome_message = ":dancer: [purple]Bem vindo ao[/purple] [red]who-unfollowed-me[/red][blue] uma implementação em Python[/blue] criada por [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Seguidores do github encontrados"
no_unfollows_message = "[green]:raised_hands: [underline]Nenhum não seguidor!"
end_message = ":fire: Você tem {follower_num} seguidores. Mantenha o bom trabalho\\n"
thankyou_message = ":pray: Obrigado por usar o projeto"

[locale.portuguese.panels]
welcome_message = ":dancer: [purple]Bem vindo ao[/purple] [red]who-unfollowed-me[/red][blue] uma implementação em Python[/blue] criada por [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Seguidores do github encontrados"
no_unfollows_message = "[white on #308012] Nenhum não seguidor! [/white on #308012]                                "
end_message = ":fire: Você tem {follower_num} seguidores. Mantenha o bom trabalho\\n"
thankyou_message = ":pray: Obrigado por usar o projeto"

[locale.portuguese.bubbles]
welcome_message_a = "[white on purple]Bem vindo ao[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]uma implementação em Python[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]criada por Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Seguidores do github encontrados[/white on cyan]"
no_unfollows_message = "[white on green4]Nenhum não seguidor![/white on green4]"
end_message_a = "[white on purple]Você tem {follower_num} seguidores.[/white on purple]"
end_message_b = "[white on magenta]Mantenha o bom trabalho![/white on magenta]"
thankyou_message = "[white on blue]Obrigado por usar o projeto[/white on blue]"


[locale.hindi]
[locale.hindi.regular]
welcome_message = ":dancer: [purple]Aapka Swagat Hai[/purple] [red]who-unfollowed-me[/red][purple]mai[/purple][blue] Python mai kaaryaanvayan [/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Github followers praapt kie gae"
no_unfollows_message = "[green]:raised_hands: [underline]Koi unfollow nahi!"
end_message = ":fire: Aapke paas {follower_num} followers hai. Acha kaam jari rakhiye\\n"
thankyou_message = ":pray: Iss project ko use karne ke liye dhanyawaad"

[locale.hindi.panels]
welcome_message = ":dancer: [purple]Aapka Swagat hai[/purple] [red]who-unfollowed-me[/red][purple]mai[/purple][blue] Python mai kaaryaanvayan [/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Github followers praapt kie gae"
no_unfollows_message = "[white on #308012]Koi unfollow nahi! [/white on #308012]                                "
end_message = ":fire: Aapke paas {follower_num} followers hai. Acha kaam jari rakhiye\\n"
thankyou_message = ":pray: Iss project ko use karne ke liye dhanyawaad"

[locale.hindi.bubbles]
welcome_message_a = "[white on purple]Aapka Swagat hai[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]Python mai kaaryaanvayan [/white on blue]"
welcome_message_d = "[white on dark_goldenrod]by Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Github followers praapt kie gae[/white on cyan]"
no_unfollows_message = "[white on green4]Koi unfollow nahi![/white on green4]"
end_message_a = "[white on purple]Aapke paas {follower_num} followers hai.[/white on purple]"
end_message_b = "[white on magenta]Acha kaam jari rakhiye![/white on magenta]"
thankyou_message = "[white on blue]Iss project ko use karne ke liye dhanyawaad[/white on blue]"

"""


def get_config() -> dict:
    global threads_stopped
    if os.path.exists(f"{UNFOLLOW_PATH}/unfollow.toml"):
        config = toml.load(f"{UNFOLLOW_PATH}/unfollow.toml")
    else:
        with open(f"{UNFOLLOW_PATH}/unfollow.toml", "w") as config_file:
            config = toml.loads(default_config)
            toml.dump(config, config_file)

    return config
