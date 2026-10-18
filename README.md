# FoturVPN Routing

Профили маршрутизации FoturVPN для **Happ** и **INCY**. Рекомендуемый профиль — `DEFAULT`.

## Быстрая установка

На телефоне откройте файл `.DEEPLINK` для нужного приложения. Если файл открылся как текст, скопируйте строку `happ://` или `incy://` и откройте её на этом же устройстве. JSON-файл можно импортировать через редактор маршрутизации приложения.

### Happ

| Профиль | Назначение | JSON | Deeplink |
|---|---|---|---|
| **DEFAULT** | Россия и Беларусь, Microsoft, Apple и выбранные игровые сервисы — напрямую; YouTube, Telegram, GitHub, Google Play и остальное — через VPN. Реклама, телеметрия Windows и BitTorrent DHT блокируются. | [JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/DEFAULT.JSON) | [DEEPLINK](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/DEFAULT.DEEPLINK) |
| **WHITELIST** | Напрямую идут только домены и IP из белых списков; остальное — через VPN. Реклама, телеметрия и BitTorrent DHT блокируются. | [JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/WHITELIST.JSON) | [DEEPLINK](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/WHITELIST.DEEPLINK) |
| **JSONSUB** | Минимальный профиль с DNS и GeoIP/Geosite. Подходит, если правила задаются отдельно в подписке или панели. | [JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/JSONSUB.JSON) | [DEEPLINK](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/JSONSUB.DEEPLINK) |

### INCY

| Профиль | Назначение | JSON | Deeplink |
|---|---|---|---|
| **DEFAULT** | Россия и Беларусь, Microsoft, Apple и выбранные игровые сервисы — напрямую; YouTube, Telegram, GitHub, Google Play и остальное — через VPN. Реклама, телеметрия Windows и BitTorrent DHT блокируются. | [JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/DEFAULT.JSON) | [DEEPLINK](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/DEFAULT.DEEPLINK) |
| **WHITELIST** | Напрямую идут только домены и IP из белых списков; остальное — через VPN. Реклама, телеметрия и BitTorrent DHT блокируются. | [JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/WHITELIST.JSON) | [DEEPLINK](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/WHITELIST.DEEPLINK) |
| **JSONSUB** | Минимальный профиль с DNS и GeoIP/Geosite. Подходит, если правила задаются отдельно в подписке или панели. | [JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/JSONSUB.JSON) | [DEEPLINK](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/JSONSUB.DEEPLINK) |

## Правила DEFAULT

| Действие | Что попадает в правило |
|---|---|
| **DIRECT** | Частные сети, российские и белорусские домены/IP, Microsoft, Apple, Steam, Epic Games, Riot, Escape from Tarkov, Twitch, Pinterest и Faceit |
| **PROXY** | Google Play/Android, YouTube, Telegram, GitHub, Twitch Ads и весь остальной трафик |
| **BLOCK** | Телеметрия Windows, публичные BitTorrent DHT и реклама |

Порядок обработки: **BLOCK → PROXY → DIRECT**.

## DNS

| Трафик | DNS |
|---|---|
| Прямой | Яндекс DNS `77.88.8.8` по DoH |
| Через VPN | Google Public DNS `8.8.8.8` по DoH |

## Списки GeoIP и Geosite

JSON-профили и deeplink-файлы FoturVPN хранятся в этом репозитории. Наборы адресов и доменов сейчас загружаются из релизов [roscomvpn-geoip](https://github.com/hydraponique/roscomvpn-geoip) и [roscomvpn-geosite](https://github.com/hydraponique/roscomvpn-geosite); ссылки на них прописаны в JSON-профилях.

GitHub Actions проверяет новые версии наборов каждую неделю, обновляет ссылки и пересобирает deeplink-файлы. Запуск вручную доступен во вкладке **Actions**.

## Файлы

- `HAPP/` и `INCY/` содержат по три профиля: `DEFAULT`, `WHITELIST`, `JSONSUB`.
- `.JSON` — профиль маршрутизации.
- `.DEEPLINK` — ссылка для импорта в соответствующее приложение.
