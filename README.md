<div align="center">

# FoturVPN Routing

**Маршрутизация для Happ и INCY**

Выберите профиль: российские и белорусские ресурсы — напрямую, нужные сервисы — через VPN, нежелательный трафик — блокируется.

![Happ](https://img.shields.io/badge/Happ-поддерживается-4776E6?style=for-the-badge)
![INCY](https://img.shields.io/badge/INCY-поддерживается-168A68?style=for-the-badge)
![Hiddify](https://img.shields.io/badge/Hiddify-настройки-7357D5?style=for-the-badge)
![Profiles](https://img.shields.io/badge/профили-DEFAULT_%7C_WHITELIST_%7C_JSONSUB-555?style=for-the-badge)

[Быстрая установка](#быстрый-старт) · [Профили](#профили) · [Правила](#что-куда-направляется) · [Обновления](#обновление-списков)

</div>

---

## 📲 Готовые ссылки для приложений

Откройте ссылку на устройстве, где установлено нужное приложение. Она ведёт на страницу FoturVPN в Vercel и передаёт настройки в приложение.

| Приложение | Готовая ссылка | Файлы и настройки |
|---|---|---|
| **Happ** | [Установить FoturVPN](https://clck.ru/3WZCbn) | [Профили Happ](#профили-happ) |
| **INCY** | [Установить FoturVPN](https://clck.ru/3WZCd7) | [Профили INCY](#профили-incy) |
| **Hiddify** | [Скачать FoturVPN.json](https://hiddify-link.vercel.app/FoturVPN.json) | [Как импортировать](#hiddify) |

Для Hiddify доступен полный JSON-файл настроек. Скачайте его и импортируйте через **Настройки → Config Options → ⋮ → Import from file**.

---

## 🚀 Быстрый старт

1. Выберите своё приложение и профиль **DEFAULT**.
2. Откройте файл **DEEPLINK** на устройстве с установленным приложением.
3. Если GitHub показывает текст ссылки, скопируйте строку `happ://` или `incy://` и откройте её на этом же устройстве.

| Приложение | Рекомендуемый профиль | JSON |
|---|---|---|
| **Happ** | [Установить DEFAULT](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/DEFAULT.DEEPLINK) | [Открыть JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/DEFAULT.JSON) |
| **INCY** | [Установить DEFAULT](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/DEFAULT.DEEPLINK) | [Открыть JSON](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/DEFAULT.JSON) |

> Deeplink импортирует настройки в приложение. Чтобы получить изменения, внесённые в профиль позднее, импортируйте его заново.

### Hiddify

[Скачайте `FoturVPN.json`](https://hiddify-link.vercel.app/FoturVPN.json), затем импортируйте его в приложении:

1. Откройте **Настройки → Config Options (Параметры конфигурации)**.
2. В меню **⋮** выберите **Import from file (Импорт из файла)**.
3. Выберите скачанный файл и подтвердите импорт.

JSON содержит полный экспорт настроек приложения, включая правила маршрутизации. Не добавляйте его через кнопку `+` в разделе VPN-профилей: используйте именно **Config Options**.

Если устройство сохранило файл как `FoturVPN.json.txt`, переименуйте его в `FoturVPN.json` перед импортом. В имени должно остаться только одно расширение `.json`.

Конфиг использует действия `direct`, `proxy` и `block`:

- **Напрямую (`direct`)** — частные сети, российские домены и IP, белые списки, Apple, Microsoft и выбранные игровые сервисы.
- **Через VPN (`proxy`)** — Google Play, GitHub, YouTube и Telegram; Twitch Ads также направляется через VPN.
- **Блокируется (`block`)** — реклама, телеметрия Windows и публичные BitTorrent DHT.
- **Остальной трафик** — идёт через VPN, если для него нет отдельного правила.

Импорт полного JSON в Hiddify может заменить соответствующие текущие параметры приложения.

## 🎛 Профили

Профили доступны для [Happ](#профили-happ) и [INCY](#профили-incy). Логика маршрутизации у них одинаковая.

### Профили Happ

| Профиль | Для чего | Deeplink | JSON |
|---|---|---|---|
| **DEFAULT** | Готовые правила на каждый день | [Установить](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/DEFAULT.DEEPLINK) | [Посмотреть](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/DEFAULT.JSON) |
| **WHITELIST** | Направлять напрямую только разрешённые домены и IP, остальное — через VPN | [Установить](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/WHITELIST.DEEPLINK) | [Посмотреть](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/WHITELIST.JSON) |
| **JSONSUB** | Базовый профиль для конфигурации, где правила задаются отдельно | [Установить](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/JSONSUB.DEEPLINK) | [Посмотреть](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/HAPP/JSONSUB.JSON) |

### Профили INCY

| Профиль | Для чего | Deeplink | JSON |
|---|---|---|---|
| **DEFAULT** | Готовые правила на каждый день | [Установить](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/DEFAULT.DEEPLINK) | [Посмотреть](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/DEFAULT.JSON) |
| **WHITELIST** | Направлять напрямую только разрешённые домены и IP, остальное — через VPN | [Установить](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/WHITELIST.DEEPLINK) | [Посмотреть](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/WHITELIST.JSON) |
| **JSONSUB** | Базовый профиль для конфигурации, где правила задаются отдельно | [Установить](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/JSONSUB.DEEPLINK) | [Посмотреть](https://raw.githubusercontent.com/Woonze/foturvpn-routing/main/INCY/JSONSUB.JSON) |

## 🧭 Что куда направляется

| Профиль | Напрямую | Через VPN | Блокируется |
|---|---|---|---|
| **DEFAULT** | Частные сети, сайты и IP России/Беларуси, Apple, Microsoft, выбранные игровые сервисы, Twitch и Faceit | YouTube, Telegram, GitHub, Google Play, реклама Twitch и остальной трафик | Реклама, телеметрия Windows, публичные BitTorrent DHT |
| **WHITELIST** | Частные сети и домены/IP из белых списков | Остальной трафик | Реклама, телеметрия Windows, публичные BitTorrent DHT |
| **JSONSUB** | Задаётся внешними правилами | Задаётся внешними правилами | Задаётся внешними правилами |

В профилях `DEFAULT` и `WHITELIST` порядок обработки правил: **BLOCK → PROXY → DIRECT**. Трафик, для которого нет отдельного правила, по умолчанию направляется через VPN.

## 🌐 DNS

| Назначение | DNS-сервер | Протокол |
|---|---|---|
| Запросы для прямого трафика | Яндекс DNS · `77.88.8.8` | DoH |
| Запросы для трафика через VPN | Google Public DNS · `8.8.8.8` | DoH |

## 🔄 Обновление списков

Профили FoturVPN используют GeoIP- и Geosite-файлы из релизов авторитетных наборов данных:

- [GeoIP](https://github.com/hydraponique/roscomvpn-geoip) — диапазоны IP-адресов.
- [Geosite](https://github.com/hydraponique/roscomvpn-geosite) — домены, сгруппированные по категориям.

GitHub Actions раз в неделю проверяет новые выпуски, обновляет ссылки в JSON-профилях и пересоздаёт deeplink-файлы. При отсутствии новых выпусков профили не меняются. [Открыть Actions](https://github.com/Woonze/foturvpn-routing/actions/workflows/update-geodata.yml) и запустить обновление можно вручную.

## 📁 Структура репозитория

```text
HAPP/   Профили и deeplink-ссылки для Happ
INCY/   Профили и deeplink-ссылки для INCY
HIDDIFY/ Настройки маршрутизации для Hiddify
```

Для Happ и INCY доступны три профиля: `.JSON` содержит настройки маршрутизации, `.DEEPLINK` — ссылку для импорта. Для Hiddify доступен полный JSON-файл настроек приложения.

---

<div align="center">

**FoturVPN · Ваш трафик — по вашим правилам**

</div>
