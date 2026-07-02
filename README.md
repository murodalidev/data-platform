# Data Engineering Template

> https://github.com/murodalidev/data-platform

Data engineering proyektlari uchun tayyor shablon: **Airflow** (orkestratsiya) + **dbt** (transformatsiya) + **Python** (ingestion), Claude Code bilan ishlashga to'liq sozlangan.

## Repoda nima bor

```
├── CLAUDE.md              # Claude har sessiyada o'qiydigan proyekt konteksti: arxitektura, printsiplar, buyruqlar
├── .claude/
│   ├── settings.json      # Claude ruxsatlari: secretlarni o'qish bloklangan, xavfli buyruqlar so'rab ishlaydi
│   ├── rules/             # Avtomatik yuklanadigan qoidalar: SQL uslubi, Python uslubi, data quality, security
│   ├── commands/          # Slash-commandlar (quyida ro'yxati)
│   ├── skills/            # Claude o'zi kerak paytda yuklaydigan workflow'lar (dbt model, DAG, DQ audit, migration)
│   └── agents/            # Subagentlar: sql-reviewer (SQL review), pipeline-debugger (faqat diagnostika)
├── specs/
│   ├── _template/         # spec.md → plan.md → tasks.md shablonlari
│   └── 001-example-.../   # to'ldirilgan namuna spec
├── dags/                  # Airflow DAG'lar — faqat orkestratsiya, logika src/ da
├── src/
│   ├── extract/           # Source konnektorlar (BaseExtractor'dan meros oladi), schemas/ — pydantic modellar
│   ├── transform/         # Warehouse'gacha bo'lgan Python transformatsiyalar (biznes-logika dbt'da!)
│   ├── load/              # Warehouse loaderlar (idempotent upsert)
│   └── utils/             # config, logging, retry, audit — hamma joyda shulardan foydalaniladi
├── dbt/
│   ├── models/staging/    # 1:1 source bilan, faqat rename/cast (stg_)
│   ├── models/intermediate/  # qayta ishlatiladigan joinlar (int_)
│   └── models/marts/      # biznesga qaratilgan modellar (fct_, dim_)
├── configs/               # Muhit bo'yicha YAML konfiglar (dev/staging/prod)
├── tests/                 # pytest, src/ strukturasini takrorlaydi
├── docker-compose.yml     # Lokal Airflow + Postgres
├── Makefile               # setup / test / lint / dbt-run / airflow-up
├── .github/workflows/     # CI: ruff + pytest + dbt parse
└── .env.example           # Kerakli env o'zgaruvchilar ro'yxati (haqiqiy .env hech qachon commit qilinmaydi)
```

## Yangi proyekt ochish

```bash
# 1. Template'dan yangi repo yaratish
gh repo create yangi-proyekt --template murodalidev/data-platform --private --clone
cd yangi-proyekt

# yoki GitHub saytida: https://github.com/murodalidev/data-platform
# → yashil "Use this template" tugmasi → "Create a new repository"

# 2. Muhitni sozlash
cp .env.example .env       # credentiallarni to'ldiring
make setup                 # uv sync
make airflow-up            # lokal Airflow: http://localhost:8080

# 3. Claude Code'ni ishga tushirish
claude
# Birinchi xabar: "Bu template'dan yaratilgan yangi proyekt, nomi: X.
# CLAUDE.md, dbt_project.yml, pyproject.toml dagi nomlarni yangila."
```

## Kundalik ish tartibi

Katta feature (yangi pipeline, yangi mart, migration) — **spec → plan → implement**:

```
/create-spec sales orders pipeline   # Claude intervyu oladi, spec.md yozadi. Kod yozmaydi.
# spec'ni o'qib approve qilasiz
/create-plan specs/002-sales-orders  # plan.md + tasks.md yaratadi
# planni approve qilasiz
/implement specs/002-sales-orders    # tasklarni bajaradi, har fazadan keyin to'xtaydi
```

Kichik fix (~30 qatordan kam, schema o'zgarmasa) — spec'siz to'g'ridan-to'g'ri.

## Slash-commandlar

| Buyruq | Nima qiladi |
|---|---|
| `/create-spec <nom>` | Yangi feature uchun spec.md (intervyu orqali) |
| `/create-plan <specs/NNN>` | Approved spec'dan plan.md + tasks.md |
| `/implement <specs/NNN>` | Tasklarni fazama-faza bajaradi |
| `/new-pipeline <manba>` | Tezkor pipeline scaffold (extractor + DAG + staging + testlar) |
| `/review-pipeline` | Branch'dagi o'zgarishlarni DE nuqtai nazaridan review (idempotentlik, backfill, PII...) |
| `/backfill-plan <model>` | Xavfsiz backfill rejasi (bajarmasdan, faqat reja) |
| `/debug-dag <dag>` | Yiqilgan DAG'ni tizimli debug qilish |
| `/dq-audit` | dbt modellarda test coverage auditi, kamchiliklar ro'yxati |

## Asosiy qoidalar (Claude ham, odam ham amal qiladi)

1. Har pipeline **idempotent** — qayta ishga tushirish dublikat yaratmaydi
2. `datetime.now()` taqiqlangan — hamma narsa `execution_date` bilan parametrlanadi (backfill uchun)
3. Biznes-logika **dbt'da**, DAG'lar faqat orkestratsiya qiladi
4. Har dbt model YAML + PK testlari (`unique`, `not_null`) bilan keladi
5. Secretlar faqat env orqali — `.env` git'ga tushmaydi, Claude uni o'qiy olmaydi

Batafsil: `CLAUDE.md` va `.claude/rules/`.
