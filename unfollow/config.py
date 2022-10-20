#!/usr/bin/evn python3

import os

import toml
from shutil import copy2

from unfollow.unfollow import UNFOLLOW_PATH

# !----------- IMPORTANT
# Due to f-strings overwriting the variable input in the config file,
# please ensure both curr_config_version in python, and "version" in the
# default_config are updated
# !----------- IMPORTANT
curr_config_version = 1
default_config = """
version=1

[appearance]

[appearance.styling] # set the theme
theme = "regular"

[appearance.emojis]
init_emoji = ":dancer:"
fetch_success_emoji = ":heavy_check_mark:"
no_unfollows_emoji = ":raised_hands:"
follow_count_emoji = ":fire:"
thankyou_emoji = ":pray:"

[locale] # language
locale = "english"

# text for each language for each theme
[locale.english]

[locale.english.simple]
welcome_message = "Welcome to who-unfollowed-me Python implementation by Zac the Wise"
fetched_followers_message = "Fetched github followers"
no_unfollows_message = "No unfollows!"
end_message = "You have {follower_num} followers. Keep up the good work\\n"
thankyou_message = "Thanks for using this project"

[locale.english.regular]
welcome_message = ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] Python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Fetched github followers"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[green]:raised_hands: [underline]No unfollows!"
end_message = ":fire: You have {follower_num} followers. Keep up the good work\\n"
thankyou_message = ":pray: Thanks for using this project"

[locale.english.panels]
welcome_message = ":dancer: [purple]Welcome to[/purple] [red]who-unfollowed-me[/red][blue] Python implementation[/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Fetched github followers"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on #308012] No unfollows! [/white on #308012]                                "
end_message = ":fire: You have {follower_num} followers. Keep up the good work\\n"
thankyou_message = ":pray: Thanks for using this project"

[locale.english.bubbles]
welcome_message_a = "[white on purple]Welcome to[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]the Python implementation[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]by Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Fetched github followers[/white on cyan]"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
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
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[green]:raised_hands: [underline]Koi unfollow nahi!"
end_message = ":fire: Aapke paas {follower_num} followers hai. Acha kaam jari rakhiye\\n"
thankyou_message = ":pray: Iss project ko use karne ke liye dhanyawaad"

[locale.hindi.panels]
welcome_message = ":dancer: [purple]Aapka Swagat hai[/purple] [red]who-unfollowed-me[/red][purple]mai[/purple][blue] Python mai kaaryaanvayan [/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Github followers praapt kie gae"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on #308012]Koi unfollow nahi! [/white on #308012]                                "
end_message = ":fire: Aapke paas {follower_num} followers hai. Acha kaam jari rakhiye\\n"
thankyou_message = ":pray: Iss project ko use karne ke liye dhanyawaad"

[locale.hindi.bubbles]
welcome_message_a = "[white on purple]Aapka Swagat hai[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]Python mai kaaryaanvayan [/white on blue]"
welcome_message_d = "[white on dark_goldenrod]by Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Github followers praapt kie gae[/white on cyan]"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on green4]Koi unfollow nahi![/white on green4]"
end_message_a = "[white on purple]Aapke paas {follower_num} followers hai.[/white on purple]"
end_message_b = "[white on magenta]Acha kaam jari rakhiye![/white on magenta]"
thankyou_message = "[white on blue]Iss project ko use karne ke liye dhanyawaad[/white on blue]"



[locale.german]
[locale.german.regular]
welcome_message = ":dancer: [purple]Wilkommen zum[/purple] [red]who-unfollowed-me[/red][blue] Python Implementierung[/blue] von [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Ihre Github-Follower wurden abgeholt"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[green]:raised_hands: [underline]Keine Unfollows!"
end_message = ":fire: Sie haben {follower_num} Follower. Weiter so\\n"
thankyou_message = ":pray: Wir danken Ihnen fuer die Nutzung des Projekts"

[locale.german.panels]
welcome_message = ":dancer: [purple]Wilkommen zum[/purple] [red]who-unfollowed-me[/red][blue] Python Implementierung[/blue] von [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Ihre Github-Follower wurden abgeholt"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on #308012] Keine Unfollows! [/white on #308012]                                "
end_message = ":fire: Sie haben {follower_num} Follower. Weiter so\\n"
thankyou_message = ":pray: Wir danken Ihnen fuer die Nutzung des Projekts"

[locale.german.bubbles]
welcome_message_a = "[white on purple]Wilkommen zum[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]die Python Implementierung[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]von Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Ihre Github-Follower wurden abgeholt[/white on cyan]"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on green4]Keine Unfollows![/white on green4]"
end_message_a = "[white on purple]Sie haben {follower_num} Follower.[/white on purple]"
end_message_b = "[white on magenta]Weiter so![/white on magenta]"
thankyou_message = "[white on blue]Wir danken Ihnen fuer die Nutzung des Projekts[/white on blue]"



[locale.french]
[locale.french.regular]
welcome_message = ":dancer: [purple]Bienvenue à[/purple] [red]who-unfollowed-me[/red][blue] version Python[/blue] par [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Abonnés GitHub récupérés"
no_unfollows_message = "[green]:raised_hands: [underline]Aucun désabonnement!"
end_message = ":fire: Vous avez {follower_num} abonnés. Continuez comme ça\\n"
thankyou_message = ":pray: Merci d'avoir utilisé ce projet"

[locale.french.panels]
welcome_message = ":dancer: [purple]Bienvenue à[/purple] [red]who-unfollowed-me[/red][blue] version Python[/blue] par [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Abonnés GitHub récupérés"
no_unfollows_message = "[white on #308012] Aucun désabonnement! [/white on #308012]                                "
end_message = ":fire: Vous avez {follower_num} abonnés. Continuez comme ça\\n"
thankyou_message = ":pray: Merci d'avoir utilisé ce projet"

[locale.french.bubbles]
welcome_message_a = "[white on purple]Bienvenue à[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]version Python[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]par Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Abonnés GitHub récupérés[/white on cyan]"
no_unfollows_message = "[white on green4]Aucun désabonnement![/white on green4]"
end_message_a = "[white on purple]Vous avez {follower_num} abonnés.[/white on purple]"
end_message_b = "[white on magenta]Continuez comme ça![/white on magenta]"
thankyou_message = "[white on blue]Merci d'avoir utilisé ce projet[/white on blue]"



[locale.turkish]
[locale.turkish.regular]
welcome_message = ":dancer: [red]who-unfollowed-me[/red][purple]'ye Hoşgeldiniz'[/purple][blue] Python uygulaması[/blue] [#FFD700]Zac the Wise[#FFD700] [blue]tarafından[/blue]"
fetched_followers_message = "[green]✔ [underline]Github takipçileri alındı"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[green]:raised_hands: [underline]Takipten çıkan kimse yok!"
end_message = ":fire: {follower_num} takipçiniz var. Böyle devam edin\\n"
thankyou_message = ":pray: Bu projeyi kullandığınız için teşekkürler"

[locale.turkish.panels]
welcome_message = ":dancer: [red]who-unfollowed-me[/red][purple]'ye Hoşgeldiniz'[/purple][blue] Python uygulaması[/blue] [#FFD700]Zac the Wise[#FFD700] [blue]tarafından[/blue]"
fetched_followers_message = "[green]✔ [underline]Github takipçileri alındı"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[green]:raised_hands: [underline]Takipten çıkan kimse yok!"
end_message = ":fire: {follower_num} takipçiniz var. Böyle devam et\\n"
thankyou_message = ":pray: Bu projeyi kullandığınız için teşekkürler"

[locale.turkish.bubbles]
welcome_message_a = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_b = "[white on purple]Hoşgeldiniz[/white on purple]"
welcome_message_c = "[white on blue]Python uygulaması[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]Zac the Wise tarafından[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Github takipçileri alındı[/white on cyan]"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on green4]Takipten çıkan kimse yok![/white on green4]"
end_message_a = "[white on purple]{follower_num} takipçiniz var.[/white on purple]"
end_message_b = "[white on magenta]Böyle devam edin![/white on magenta]"
thankyou_message = "[white on blue]Bu projeyi kullandığınız için teşekkürler[/white on blue]"




[locale.spanish]
[locale.spanish.regular]
welcome_message = ":dancer: [purple]Bienvenido a[/purple] [red]who-unfollowed-me[/red][blue] versión Python[/blue] por [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Recuperación de los seguidores GitHub"
no_unfollows_message = "[green]:raised_hands: [underline]¡Ningún seguidor dado de baja!"
end_message = ":fire: Tienes {follower_num} seguidores. Sigue así\\n"
thankyou_message = ":pray: Gracias por utilizar este proyecto"

[locale.spanish.panels]
welcome_message = ":dancer: [purple]Bienvenido a[/purple] [red]who-unfollowed-me[/red][blue] versión Python[/blue] por [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Recuperación de los seguidores GitHub"
no_unfollows_message = "[white on #308012] ¡Ningún seguidor dado de baja! [/white on #308012]                                "
end_message = ":fire: Tienes {follower_num} seguidores. Sigue así\\n"
thankyou_message = ":pray: Gracias por utilizar este proyecto"

[locale.spanish.bubbles]
welcome_message_a = "[white on purple]Bienvenido a[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]versión Python[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]por Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Recuperación de los seguidores GitHub[/white on cyan]"
no_unfollows_message = "[white on green4]¡Ningún seguidor dado de baja![/white on green4]"
end_message_a = "[white on purple]Tienes {follower_num} seguidores.[/white on purple]"
end_message_b = "[white on magenta]¡Sigue así![/white on magenta]"
thankyou_message = "[white on blue]Gracias por utilizar este proyecto[/white on blue]"


[locale.polish]
[locale.polish.regular]
welcome_message = ":dancer: [purple]Witaj w[/purple] [red]who-unfollowed-me[/red][blue] Pythonowej implementacji[/blue] stworzonej przez [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Pobrano followersów na Githubie"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[green]:raised_hands: [underline]Nikt nie przestał Cię obserwować!"
end_message = ":fire: Masz {follower_num} followersów. Działaj dalej!\\n"
thankyou_message = ":pray: Dzięki, że korzystasz z tego projektu"

[locale.polish.panels]
welcome_message = ":dancer: [purple]Witaj w[/purple] [red]who-unfollowed-me[/red][blue] Pythonowej implementacji[/blue] stworzonej przez [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Pobrano followersów na Githubie"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on #308012] Nikt nie przestał Cię obserwować! [/white on #308012]                                "
end_message = ":fire: Masz {follower_num} followersów. Działaj dalej!    \\n"
thankyou_message = ":pray: Dzięki, że korzystasz z tego projektu"

[locale.polish.bubbles]
welcome_message_a = "[white on purple]Witaj w[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]Pythonowej implementacji[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]stworzonej przez Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Pobrano followersów na Githubie[/white on cyan]"
last_week_unfollowers = "[purple]✔ [underline]Unfollowers from last week"
no_unfollows_message = "[white on green4]Nikt nie przestał Cię obserwować![/white on green4]"
end_message_a = "[white on purple]Masz {follower_num} followersów.[/white on purple]"
end_message_b = "[white on magenta]Działaj dalej![/white on magenta]"
thankyou_message = "[white on blue]Dzięki, że korzystasz z tego projektu[/white on blue]"

[locale.indonesian]
[locale.indonesian.regular]
welcome_message = ":dancer: [purple]Selamat datang ke[/purple] [red]who-unfollowed-me[/red][blue]implementasi Python[/blue] oleh [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Pengikut GitHub diambil"
no_unfollows_message = "[green]:raised_hands: [underline]Tidak ada yang berhenti mengikuti!"
end_message = ":fire: Kamu mempunyai {follower_num} pengikut. Kerja bagus\\n"
thankyou_message = ":pray: Terima kasih telah menggunakan proyek ini"

[locale.indonesian.panels]
welcome_message = ":dancer: [purple]Selamat datang ke[/purple] [red]who-unfollowed-me[/red][blue] implementasi Python[/blue] oleh [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]Pengikut GitHub berhasil diambil"
no_unfollows_message = "[white on #308012] Tidak ada yang berhenti mengikuti! [/white on #308012]                                "
end_message = ":fire: Kamu mempunyai {follower_num} pengikut. Kerja bagus\\n"
thankyou_message = ":pray: Terimakasih telah menggunakan proyek ini"

[locale.indonesian.bubbles]
welcome_message_a = "[white on purple]Selamat datang ke[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]implementasi Python [/white on blue]"
welcome_message_d = "[white on dark_goldenrod]oleh Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]Pengikut GitHub diambil [/white on cyan]"
no_unfollows_message = "[white on green4] Tidak ada yang berhenti mengikuti![/white on green4]"
end_message_a = "[white on purple]Kamu punya {follower_num} pengikut.[/white on purple]"
end_message_b = "[white on magenta]Kerja bagus![/white on magenta]"
thankyou_message = "[white on blue]Terima kasih telah menggunakan proyek ini[/white on blue]"


[locale.tamil.regular]
welcome_message = ":dancer: [purple]நல்வரவு[/purple] [red]யார் என்னை பின் தொடரவில்லை[/red][blue] பைதான் செயல்படுத்தல் [/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]கிதுப் பின்தொடர்பவர்களைப் பெற்றனர்"
no_unfollows_message = "[green]:raised_hands: [underline]பின்தொடரவில்லை!"
end_message = ":fire: உங்களிடம் உள்ள {follower_num} பின்பற்றுபவர்கள். நற்பணியை தக்கவைத்துக்கொள்ளவும்\\n"
thankyou_message = ":pray: இந்தத் திட்டத்தைப் பயன்படுத்தியதற்கு நன்றி"

[locale.tamil.panels]
welcome_message = ":dancer: [purple]நல்வரவு[/purple] [red]யார் என்னை பின் தொடரவில்லை[/red][blue] பைதான் செயல்படுத்தல்[/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]கிதுப் பின்தொடர்பவர்களைப் பெற்றனர்"
no_unfollows_message = "[white on #308012] பின்தொடரவில்லை! [/white on #308012]                                "
end_message = ":fire: உங்களிடம் உள்ள {follower_num} பின்பற்றுபவர்கள். நற்பணியை தக்கவைத்துக்கொள்ளவும்\\n"
thankyou_message = ":pray: இந்தத் திட்டத்தைப் பயன்படுத்தியதற்கு நன்றி"

[locale.tamil.bubbles]
welcome_message_a = "[white on purple]நல்வரவு[/white on purple]"
welcome_message_b = "[white on red]யார் என்னை பின் தொடரவில்லை[/white on red]"
welcome_message_c = "[white on blue]பைதான் செயல்படுத்தல்[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]by Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]கிதுப் பின்தொடர்பவர்களைப் பெற்றனர்[/white on cyan]"
no_unfollows_message = "[white on green4]பின்தொடரவில்லை![/white on green4]"
end_message_a = "[white on purple]உங்களிடம் உள்ள {follower_num} followers.[/white on purple]"
end_message_b = "[white on magenta]நற்பணியை தக்கவைத்துக்கொள்ளவும்![/white on magenta]"
thankyou_message = "[white on blue]இந்தத் திட்டத்தைப் பயன்படுத்தியதற்கு நன்றி[/white on blue]"


[locale.chinese]
[locale.chinese.simple]
welcome_message = "欢迎使用who-unfollowed-me Python开发，作者Zac the Wise"
fetched_followers_message = "获取github关注列表"
no_unfollows_message = "无取消关注！"
end_message = "有{follower_num}个人关注了你。干得不错\\n"
thankyou_message = "感谢使用本项目"

[locale.chinese.regular]
welcome_message = ":dancer: [purple]欢迎使用[/purple][red]who-unfollowed-me[/red][blue] Python开发[/blue]，作者[#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]获取github关注列表"
last_week_unfollowers = "[purple]✔ [underline]上周的取消关注"
no_unfollows_message = "[green]:raised_hands: [underline]无取消关注！"
end_message = ":fire: 有{follower_num}个人关注了你。干得不错\\n"
thankyou_message = ":pray: 感谢使用本项目"

[locale.chinese.panels]
welcome_message = ":dancer: [purple]欢迎使用[/purple][red]who-unfollowed-me[/red][blue] Python开发[/blue]，作者[#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]获取github关注列表"
last_week_unfollowers = "[purple]✔ [underline]上周的取消关注"
no_unfollows_message = "[white on #308012]无取消关注！ [/white on #308012]                                "
end_message = ":fire: 有{follower_num}个人关注了你。干得不错\\n"
thankyou_message = ":pray: 感谢使用本项目"

[locale.chinese.bubbles]
welcome_message_a = "[white on purple]欢迎使用[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]使用Python开发[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]作者Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]获取github关注列表[/white on cyan]"
last_week_unfollowers = "[purple]✔ [underline]上周的取消关注"
no_unfollows_message = "[white on green4]无取消关注！[/white on green4]"
end_message_a = "[white on purple]有{follower_num}个人关注了你。[/white on purple]"
end_message_b = "[white on magenta]干得不错！[/white on magenta]"
thankyou_message = "[white on blue]感谢使用本项目[/white on blue]"

[locale.gujarati]
[locale.gujarati.simple]
welcome_message = "કોણ અનફોલો કરે છે-માં તમારું સ્વાગત છે. "
fetched_followers_message = "fetched ગિટહબ ના ફોલોવર્સ"
no_unfollows_message = "કોઈ અનફોલો નથી. "
end_message = "તમારી પાસે {follower_num} ફોલોવોર્સ. સારું કામ ચાલુ રાખો \\n"
thankyou_message = "આ પ્રોજેક્ટ નો ઉપયોગ કરવા બદલ આભાર. "
[locale.gujarati.regular]
welcome_message = ":dancer: [purple]સ્વાગત છે.[/purple] [red]who-unfollowed-me[/red][blue] Python અમલીકરણ[/blue] માં  [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]અનાયન કરેલ  github ફોલોવર્સ"
last_week_unfollowers = "[purple]✔ [underline]છેલા અઠવાડિયા ના અનફોલોવર્સ"
no_unfollows_message = "[green]:raised_hands: [underline]કોઈ અનફોલો નથી!"
end_message = ":fire: તમારી પાસે {follower_num} ફોલોવર્સ. સારું કામ ચાલુ રાખો \\n"
thankyou_message = ":pray: આ પ્રોજેક્ટ નો ઉપયોગ કરવા બદલ આભાર."
[locale.gujarati.panels]
welcome_message = ":dancer: [purple]સ્વાગત છે.[/purple] [red]who-unfollowed-me[/red][blue] Python અમલીકરણ[/blue] by [#FFD700]Zac the Wise[#FFD700]"
fetched_followers_message = "[green]✔ [underline]અનાયન કરેલ  github ફોલોવર્સ"
last_week_unfollowers = "[purple]✔ [underline]છેલા અઠવાડિયા ના અનફોલોવર્સ"
no_unfollows_message = "[white on #308012] કોઈ અનફોલો નથી! [/white on #308012]                                "
end_message = ":fire: તમારી પાસે {follower_num} ફોલોવર્સ. સારું કામ ચાલુ રાખો \\n"
thankyou_message = ":pray: આ પ્રોજેક્ટ નો ઉપયોગ કરવા બદલ આભાર."
[locale.english.bubbles]
welcome_message_a = "[white on purple]સ્વાગત છે.[/white on purple]"
welcome_message_b = "[white on red]who-unfollowed-me[/white on red]"
welcome_message_c = "[white on blue]the Python અમલીકરણ[/white on blue]"
welcome_message_d = "[white on dark_goldenrod]by Zac the Wise[/white on dark_goldenrod]"
fetched_followers_message = "[white on cyan]અનાયન કરેલ  github ફોલોવર્સ[/white on cyan]"
last_week_unfollowers = "[purple]✔ [underline]છેલા અઠવાડિયા ના અનફોલોવર્સ"
no_unfollows_message = "[white on green4]કોઈ અનફોલો નથી![/white on green4]"
end_message_a = "[white on purple]તમારી પાસે {follower_num} followers.[/white on purple]"
end_message_b = "[white on magenta]Keep up the good work![/white on magenta]"
thankyou_message = "[white on blue]આ પ્રોજેક્ટ નો ઉપયોગ કરવા બદલ આભાર.[/white on blue]"
"""

# Future proof by allowing different messages for different versions
version_messages = {
    0: f"A breaking change required your configuration file (found at {UNFOLLOW_PATH}/unfollow.toml) to be recreated,\
    \nA copy of your previous config has been saved at {UNFOLLOW_PATH}/invalid_unfollow.toml, and your current configuration has been overwritten with a valid one.",
    "_": f"It looks like something has gone wrong with your configuration file.\
    \nA copy has been saved at {UNFOLLOW_PATH}/invalid_unfollow.toml, , and your current configuration has been overwritten with a valid one.",
}


def get_config(overwrite=False) -> dict:
    global threads_stopped

    # Ensure directory exists before creating file
    if not os.path.exists(f"{UNFOLLOW_PATH}"):
        os.mkdir(UNFOLLOW_PATH)

    if os.path.exists(f"{UNFOLLOW_PATH}/unfollow.toml") and not overwrite:
        config = toml.load(f"{UNFOLLOW_PATH}/unfollow.toml")
    elif overwrite:
        with open(
            f"{UNFOLLOW_PATH}/unfollow.toml", "w", encoding="utf-8"
        ) as config_file:
            config = toml.loads(default_config)
            toml.dump(config, config_file)
    else:
        with open(
            f"{UNFOLLOW_PATH}/unfollow.toml", "w", encoding="utf-8"
        ) as config_file:
            config = toml.loads(default_config)
            toml.dump(config, config_file)

    return config


def config_version_handle(version) -> bool:
    if version == curr_config_version:
        return False

    # If we reach here we must either have no version (version param = 0) or the version it outdated
    # thus, the config must be copied and replaced with the default
    copy2(f"{UNFOLLOW_PATH}/unfollow.toml", f"{UNFOLLOW_PATH}/invalid_unfollow.toml")

    _ = get_config(overwrite=True)

    if version not in version_messages.keys():
        version = "_"

    print(version_messages[version])
    return True
