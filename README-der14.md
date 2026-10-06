# Dərs 14 — Tag API (tapşırığın həlli)

Bu qovluq təqdim edilmiş **Step-Django-FBV-CBV-main** layihəsinin üzərində qurulub. Əsas arxivdə `api/`, `pyproject.toml`, `uv.lock` yox idi; ona görə `api/` tətbiqi, `Post` və `Category` API-si də əlavə edilib. Saytın `blog/` və `accounts/` tətbiqləri dəyişdirilməyib.

## Quraşdırma

1. İnternet bağlantısı olan kompüterdə `uv sync` komandasını icra edin. Əgər platformanız üçün paket paylanması seçilməsə, əvvəl `uv lock`, sonra `uv sync` icra edin.
2. `uv run manage.py migrate`
3. `uv run manage.py loaddata blog/fixtures/demo_full.json`
4. `uv run manage.py runserver`
5. Sayt: `http://127.0.0.1:8000/`; API: `http://127.0.0.1:8000/api/tags/`

> Qeyd: Paylaşılan arxivdə hazır SQLite bazası yoxdur. `demo_full.json` 5 dərc olunmuş post, 3 kateqoriya, 5 teq ehtiva edir. Tapşırıqda göstərilən 9/3/5 rəqəmləri yalnız nümunədir; faktiki nəticə bazaya uyğun hesablanır.

## API endpoint-ləri

| Metod | Ünvan | Gözlənilən nəticə |
| --- | --- | --- |
| GET | `/api/tags/` | 200, teq siyahısı |
| POST | `/api/tags/` | 201, yeni teq |
| GET | `/api/tags/1/` | 200, teq |
| GET | `/api/tags/99/` | 404, teq tapılmadı |
| PUT | `/api/tags/1/` | 200, yenilənmiş teq |
| DELETE | `/api/tags/1/` | 204, boş cavab |
| GET | `/api/stats/` | 200, `post_count/category_count/tag_count` |
| GET/POST | `/api/posts/` | Post siyahısı / yeni post |
| GET/PUT/DELETE | `/api/posts/1/` | Bir post |
| GET/POST | `/api/categories/` | Kateqoriya siyahısı / yaradılması |
| GET/PUT/DELETE | `/api/categories/1/` | Bir kateqoriya |

Yeni teq üçün JSON: `{"name": "vscode", "slug": "vscode"}`. Eyni `slug` təkrarından ötrü serializer 400 qaytarır.

## Yoxlama

`uv run manage.py test api` və `uv run manage.py check`.

`postman/step-blog.postman_collection.json` Postman Collection v2.1 formatında **6** istəyi ehtiva edir. Postman: Import -> faylı seçin.

## Commit və GitHub

Yalnız arxiv göndərildiyi üçün GitHub hesabınıza push edilməyib. Dəyişikliklər üç ayrı lokal commitlə hazırlanıb: **tag list**, **tag detail**, **stats**. `git-patches/` içindəki patch-lər eyni başlanğıc layihəyə ardıcıl tətbiq oluna bilər. Eyni GitHub repoda işləyirsinizsə, patch-ləri öz repoda tətbiq edib `git push` edin. `.venv/`, `db.sqlite3` gitə əlavə edilmir.

## Texniki qeyd

Hazırlanan mühitdə paket indeksinə internet çıxışı olmadığından real Django testlərini işə salmaq mümkün olmayıb. `uv.lock` içində PyPI distribusiya URL-ləri əlavə edilib və lokal olaraq pars olunur; burada internet olmadığı üçün `uv sync` və Django testləri tam icra edilməyib. Lazım gələrsə, `uv lock` ilə platformaya uyğun wheel siyahısını yeniləyin. Sintaksis və statik yoxlamalar aparılıb.
