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



[locale.german]
[locale.german.regular]
welcome_message = ":dancer: [purple]Wilkommen zum[/purple] [red]who-unfollowed-me[/red][blue] Python Implementierung[/blue] von [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Ihre Github-Follower wurden abgeholt"
no_unfollows_message = "[green]:raised_hands: [underline]Keine Unfollows!"
end_message = ":fire: Sie haben {follower_num} Follower. Weiter so\\n"
thankyou_message = ":pray: Wir danken Ihnen fuer die Nutzung des Projekts"

[locale.german.panels]
welcome_message = ":dancer: [purple]Wilkommen zum[/purple] [red]who-unfollowed-me[/red][blue] Python Implementierung[/blue] von [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Ihre Github-Follower wurden abgeholt"
no_unfollows_message = "[white on #308012] Keine Unfollows! [/white on #308012]                                "
end_message = ":fire: Sie haben {follower_num} Follower. Weiter so\\n"
thankyou_message = ":pray: Wir danken Ihnen fuer die Nutzung des Projekts"

[locale.german.bubbles]
welcome_message_a = "[white on purple]Wilkommen zum[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]die Python Implementierung[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]von Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Ihre Github-Follower wurden abgeholt[/white on cyan]"
no_unfollows_message = "[white on green4]Keine Unfollows![/white on green4]"
end_message_a = "[white on purple]Sie haben {follower_num} Follower.[/white on purple]"
end_message_b = "[white on magenta]Weiter so![/white on magenta]"
thankyou_message = "[white on blue]Wir danken Ihnen fuer die Nutzung des Projekts[/white on blue]"



[locale.french]
[locale.french.regular]
welcome_message = ":dancer: [purple]Bienvenue à[/purple] [red]who-unfollowed-me[/red][blue] Python Lamise en oeuvre[/blue] par [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Récupéré github suiveurs"
no_unfollows_message = "[green]:raised_hands: [underline]Aucun désabonnement!"
end_message = ":fire: Vous avez {follower_num} suiveurs. Continuez votre bon travail\\n"
thankyou_message = ":pray: Merci d'avoir utilisé ce projet"

[locale.french.panels]
welcome_message = ":dancer: [purple]Bienvenue à[/purple] [red]who-unfollowed-me[/red][blue] Python Lamise en oeuvre[/blue] par [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Récupéré github suiveurs"
no_unfollows_message = "[white on #308012] Aucun désabonnement! [/white on #308012]                                "
end_message = ":fire: Vous avez {follower_num} suiveurs. Continuez votre bon travail\\n"
thankyou_message = ":pray: Merci d'avoir utilisé ce projet"

[locale.french.bubbles]
welcome_message_a = "[white on purple]Bienvenue à[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]la Python lamise en oeuvre[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]par Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Récupéré github suiveurs[/white on cyan]"
no_unfollows_message = "[white on green4]Aucun désabonnement![/white on green4]"
end_message_a = "[white on purple]Vous avez {follower_num} suiveurs.[/white on purple]"
end_message_b = "[white on magenta]Continuez votre bon travail![/white on magenta]"
thankyou_message = "[white on blue]Merci d'avoir utilisé ce projet[/white on blue]"



[locale.turkish]
[locale.turkish.regular]
welcome_message = ":dancer: [red]who-unfollowed-me[/red][purple]'ye Hoşgeldiniz'[/purple][blue] Python uygulaması[/blue] [#FFD700]Zac the Wise[#FFD700] [blue]tarafından[/blue]"
fetched_followers_message = "[green]✔ [underline]Github takipçileri alındı"
no_unfollows_message = "[green]:raised_hands: [underline]Takipten çıkan kimse yok!"
end_message = ":fire: {follower_num} takipçiniz var. Böyle devam edin\\n"
thankyou_message = ":pray: Bu projeyi kullandığınız için teşekkürler"

[locale.turkish.panels]
welcome_message = ":dancer: [red]who-unfollowed-me[/red][purple]'ye Hoşgeldiniz'[/purple][blue] Python uygulaması[/blue] [#FFD700]Zac the Wise[#FFD700] [blue]tarafından[/blue]"
fetched_followers_message = "[green]✔ [underline]Github takipçileri alındı"
no_unfollows_message = "[green]:raised_hands: [underline]Takipten çıkan kimse yok!"
end_message = ":fire: {follower_num} takipçiniz var. Böyle devam et\\n"
thankyou_message = ":pray: Bu projeyi kullandığınız için teşekkürler"

[locale.turkish.bubbles]
welcome_message_a = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_b = "[white on purple]Hoşgeldiniz[/white on purple]"
welcome_message_c = "[white on blue]Python uygulaması[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]Zac the Wise tarafından[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Github takipçileri alındı[/white on cyan]"
no_unfollows_message = "[white on green4]Takipten çıkan kimse yok![/white on green4]"
end_message_a = "[white on purple]{follower_num} takipçiniz var.[/white on purple]"
end_message_b = "[white on magenta]Böyle devam edin![/white on magenta]"
thankyou_message = "[white on blue]Bu projeyi kullandığınız için teşekkürler[/white on blue]"



[locale.polish]
[locale.polish.regular]
welcome_message = ":dancer: [purple]Witaj w[/purple] [red]who-unfollowed-me[/red][blue] Pythonowej implementacji[/blue] stworzonej przez [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Pobrano followersów na Githubie"
no_unfollows_message = "[green]:raised_hands: [underline]Nikt nie przestał Cię obserwować!"
end_message = ":fire: Masz {follower_num} followersów. Działaj dalej!\\n"
thankyou_message = ":pray: Dzięki, że korzystasz z tego projektu"

[locale.polish.panels]
welcome_message = ":dancer: [purple]Witaj w[/purple] [red]who-unfollowed-me[/red][blue] Pythonowej implementacji[/blue] stworzonej przez [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Pobrano followersów na Githubie"
no_unfollows_message = "[white on #308012] Nikt nie przestał Cię obserwować! [/white on #308012]                                "
end_message = ":fire: Masz {follower_num} followersów. Działaj dalej!    \\n"
thankyou_message = ":pray: Dzięki, że korzystasz z tego projektu"

[locale.polish.bubbles]
welcome_message_a = "[white on purple]Witaj w[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]Pythonowej implementacji[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]stworzonej przez Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Pobrano followersów na Githubie[/white on cyan]"
no_unfollows_message = "[white on green4]Nikt nie przestał Cię obserwować![/white on green4]"
end_message_a = "[white on purple]Masz {follower_num} followersów.[/white on purple]"
end_message_b = "[white on magenta]Działaj dalej![/white on magenta]"
thankyou_message = "[white on blue]Dzięki, że korzystasz z tego projektu[/white on blue]"

"""


def get_config() -> dict:
    global threads_stopped
    if os.path.exists(f"{UNFOLLOW_PATH}/unfollow.toml"):
        config = toml.load(f"{UNFOLLOW_PATH}/unfollow.toml")
    else:
        with open(f"{UNFOLLOW_PATH}/unfollow.toml", "w", encoding='utf-8') as config_file:
            config = toml.loads(default_config)
            toml.dump(config, config_file)

    return config
