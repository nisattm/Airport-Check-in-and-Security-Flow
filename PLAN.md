# Proje Planı: Airport Check-in and Security Flow

**Ders:** SENG-331 Modelling and Simulation with Python
**Proje:** Proje 2, Airport Check-in and Security Flow (SimPy ile ayrık olay simülasyonu)
**Ekip:** Ceren Yüksel, Burkay Çakar, Nisa Atım
**Teslim:** 16 Aralık (Jupyter notebook) · **Demo:** 21–22 veya 28–29 Aralık, ders saatinde

---

## 1. Bizden ne isteniyor? (özet)

| # | Teslim / içerik | Nerede |
|---|---|---|
| 1 | **Event Graph** çizimi | Notebook içinde (resim olarak) |
| 2 | **Python + SimPy** ile ayrık olay simülasyonu | Notebook içinde |
| 3 | **Jupyter notebook**: açıklamalı, yorumlu. Event graph ve SimPy kodu ikisi de içinde | Teslim edilen dosya |
| 4 | **Sınıf içi sunum**: tasarım (event graph) + simülasyon | Son iki hafta, ders saati |
| ★ | **%10 bonus:** simülasyonun **2D/3D animasyonu** (kesin yapıyoruz) | Notebook + demo |

**Bütün projeler için zorunlu çıktılar** (her kuyruk / her hizmet noktası için):
- Her kuyrukta ortalama gecikme (check-in kuyruğu, güvenlik kuyruğu)
- Sistemde ortalama kalış süresi
- Her kuyruktaki zaman-ortalamalı kişi sayısı
- Sistemdeki zaman-ortalamalı kişi sayısı
- Her hizmet noktasının sunucu kullanım oranı (utilization)
- **B(t)** grafikleri (her hizmet noktası için meşgul sunucu sayısı)
- **Q(t)** grafikleri (her kuyruk için kuyruk uzunluğu)

**Deney tasarımı:**
- Başlangıç tahmini kadar (ör. n₀ = 10) bağımsız replikasyon. Her kuyruğun ortalama gecikmesi için güven aralığı (%95).
- Hata payı **β** için gereken replikasyon sayısını bulmak, ek replikasyonları çalıştırıp güven aralıklarını güncellemek.
- Seçilen faktörlerin çıktılara etkisini incelemek.

**Proje 2'ye özel:**
- Varışlar: üstel, ortalama 1,5 dk (λ ≈ 0,667 yolcu/dk)
- Check-in: 5 masa, üstel hizmet, ortalama 4 dk
- Güvenlik: 3 tarayıcı, üstel hizmet, ortalama 5 dk
- Ek çıktılar: check-in kuyruğunda ortalama bekleme, sistemde ortalama toplam süre, **maksimum kuyruk uzunluğu**, check-in ve güvenlik personelinin kullanım oranı
- Faktörler: check-in masası sayısı **(3, 5)**, güvenlik tarayıcısı sayısı **(2, 4)**

### %10 bonus: animasyon (kesin yapılacak)
Hocanın metninde %10 ile ilgili tek ifade şu:
> "You will get 10% bonus if you implement an animation of the simulation problem using a 2D or 3D environment"

Yani ek puanı **simülasyonun 2D/3D animasyonu** getiriyor. **Bu kısmı kesin olarak yapıyoruz.** Bizim için isteğe bağlı değil, diğer zorunlu teslimlerle aynı önemde. C hattının parçası (bkz. Bölüm 5): Faz 2'de ilk çalışan sürüm, Faz 3'te bitmiş hali. Teslim edilen notebook'ta (Bölüm 9) ve demoda gösterilecek.

### Projenin tam tanımı (ekip arkadaşları ve Claude için bağlam)

> Bu bölüm tek başına okunabilecek şekilde yazıldı. Projeye yeni başlayan bir ekip üyesi ya da Claude oturumu önce bu bölümü okumalı. Kendi Claude'unuza bu bölümü (veya PLAN.md'nin tamamını) verip "ben X hattındayım, faz N'deyim" demeniz yeterli.

**1. Ders ve görev.** SENG-331 "Modelling and Simulation with Python" dersinin dönem projesi. Hocanın verdiği 20 projeden **Proje 2: Airport Check-in and Security Flow**'u seçtik. 3 kişilik ekibiz: Ceren Yüksel, Burkay Çakar, Nisa Atım. Python ve **SimPy** ile bir ayrık olay simülasyonu yapacağız.

**2. Hocanın sistem tanımı (proje metninden, değiştirilemez).**
- Yolcular havalimanına gelir. Önce check-in masalarından birinde işlem yaptırır, sonra güvenlik taramasına geçer. Masa ve tarayıcı sayısı sınırlıdır.
- Varışlar arası süre: üstel dağılım, ortalama 1,5 dk
- Check-in: 5 masa, hizmet süresi üstel, ortalama 4 dk
- Güvenlik: 3 tarayıcı, hizmet süresi üstel, ortalama 5 dk
- Deney faktörleri: check-in masası sayısı (3, 5) ve güvenlik tarayıcısı sayısı (2, 4)

**3. Teslim edilecekler (proje metninden).**
1. Problemin **Event Graph**'ı çizilecek.
2. Ayrık olay programı **Python + SimPy** ile yazılacak.
3. Açıklamalı ve yorumlu tek bir **Jupyter notebook** teslim edilecek. Event graph ve SimPy kodu ikisi de notebook'ta olacak. Teslim tarihi 16 Aralık.
4. Tasarım ve uygulama derste sunulacak (21–22 veya 28–29 Aralık).
5. ★ **%10 bonus:** simülasyonun 2D veya 3D animasyonu. Biz bunu **kesin yapıyoruz**, zorunlu teslim gibi ele alınmalı.

**4. Hesaplanacak çıktılar (proje metninden).** Check-in ve güvenlik için ayrı ayrı:
- kuyruktaki ortalama gecikme (bekleme süresi), kuyruktaki zaman-ortalamalı kişi sayısı, **maksimum kuyruk uzunluğu**
- sunucu kullanım oranı ve **B(t)** grafiği (meşgul sunucu sayısı), **Q(t)** grafiği (kuyruk uzunluğu)

Sistemin tamamı için: sistemde ortalama kalış süresi ve sistemdeki zaman-ortalamalı kişi sayısı.

**5. Deney ve istatistik (proje metninden).**
- Başlangıç replikasyon sayısıyla (n₀) çalıştırıp **her kuyruğun ortalama gecikmesi için güven aralığı** hesaplanacak. Güven düzeyini biz seçiyoruz: %95.
- Hata payı **β** için gereken replikasyon sayısı (n*) bulunacak ve güven aralıkları n* replikasyonla yeniden hesaplanacak.
- Faktörlerin (masa ve tarayıcı sayısı) çıktılara etkisi incelenecek.

**6. Bizim aldığımız kararlar (proje metninde yok, gerekçeleri Bölüm 2 ve 4'te).**
- **Simülasyon türü: terminating.** 3 tarayıcıda güvenlik kapasitesi (0,6 yolcu/dk) varış hızından (0,667 yolcu/dk) düşük, yani kuyruk sınırsız büyüyor ve kararlı durum yok. Bu yüzden terminal **1440 dk (1 gün)** yolcu kabul ediyor, sonra varışlar duruyor ve sistem boşalınca simülasyon bitiyor. Her replikasyon bir gün.
- **Deneyler:** temel senaryo (5 masa, 3 tarayıcı) + 2×2 tam faktöriyel (masa {3,5} × tarayıcı {2,4}) = 5 konfigürasyon (`config.EXPERIMENTS`).
- **İstatistik ayarları:** n₀ = 10, güven düzeyi %95, β = 1,0 dk, replikasyon r için tohum = 42 + r.
- **Doğrulama:** Kararlı istasyonlar (5 masalı check-in, 4 tarayıcılı güvenlik) teorik M/M/c (Erlang-C) değerleriyle karşılaştırılacak.
- **Animasyon:** `RunResult.event_log` kaydı matplotlib animasyonuyla oynatılıyor (masalar, tarayıcılar, kuyruklar, saat), GIF/MP4 olarak kaydediliyor.
- Varsayımlar: her istasyonda tek ortak FIFO kuyruk, istasyonlar arası yürüme süresi 0, herkes check-in yapıyor, kuyruktan ayrılan yok, arıza ve mola yok.

**7. Kod yapısı ve sabit arayüzler.** Kod `src/airport_sim/` içinde, teslim notebook'u `notebooks/Airport_Checkin_Security.ipynb`.
- `config.py`: bütün parametreler `Config` sınıfında, deneyler `EXPERIMENTS` listesinde. Parametreler başka yerde sabit olarak yazılmaz.
- `model.py`: `run_simulation(config, seed) -> RunResult`. `RunResult` alanları ve `event_log` olay adları (`ARRIVAL`, `START_CHECKIN`, `END_CHECKIN`, `START_SECURITY`, `DEPARTURE`) **sabit**.
- `monitor.py`: `summarize(run) -> dict`, anahtarları `METRIC_KEYS` içinde sabit.
- `analysis.py`: `replicate`, `confidence_interval`, `required_replications`, `run_experiments`
- `plots.py`, `animation.py`
- Bu arayüzleri değiştirmek gerekirse önce ekibe haber verilir, çünkü diğer hatlar onlara göre paralel çalışıyor.

**8. Çalışma düzeni.** İş üç hatta bölündü: **A Model**, **B Analiz**, **C Tasarım ve animasyon**. Üç faz var. Her fazda herkes farklı bir hatta çalışıyor, faz sonunda `docs/handoff/` altına devir notu yazıp PR açıyor, hattı devralan kişi PR'ı inceleyip kaldığı yerden devam ediyor (ayrıntı Bölüm 5).

**9. Claude için kurallar.**
- Dil: Bu plan (PLAN.md) Türkçe. Repodaki **diğer her şey İngilizce**: kod, yorumlar, notebook açıklamaları, dokümanlar, commit mesajları ve PR'lar (ders İngilizce).
- Kendi hattının dışındaki dosyalarda büyük değişiklik yapma. Gerekirse devir notuna veya PR açıklamasına yaz.
- Projeye yalnızca proje metninin istediklerini ve bu planda aldığımız kararları koy. Metinde verilmeyen bir değer gerekiyorsa senaryoya göre en mantıklısını seç ve gerekçesini yaz.

---

## 2. Önemli bir tasarım kararı: sistem **kararsız**, bu yüzden "terminating" simülasyon

Kapasite hesabı (λ = 1/1,5 = 0,667 yolcu/dk):

| İstasyon | Sunucu | Kapasite (yolcu/dk) | ρ = λ / kapasite | Durum |
|---|---|---|---|---|
| Check-in | 3 masa | 3/4 = 0,75 | 0,89 | Kararlı ama yoğun |
| Check-in | 5 masa | 5/4 = 1,25 | 0,53 | Rahat |
| Güvenlik | 2 tarayıcı | 2/5 = 0,40 | **1,67** | **Kararsız**, kuyruk sürekli büyür |
| Güvenlik | 3 tarayıcı (temel) | 3/5 = 0,60 | **1,11** | **Kararsız** |
| Güvenlik | 4 tarayıcı | 4/5 = 0,80 | 0,83 | Kararlı |

Temel senaryoda güvenlik kuyruğu zamanla sınırsız büyüyor. Bu yüzden kararlı durum (steady-state) ortalaması anlamlı değil. **Terminating simulation** kullanıyoruz:

- **Başlangıç koşulu:** Sistem boş, bütün masalar ve tarayıcılar boşta.
- **Çalışma süresi:** Terminal **1440 dk (1 tam gün)** boyunca yolcu kabul eder.
- **Sonlanma olayı E:** "1440 dk geçti **ve** sistemde yolcu kalmadı." Kapı kapandıktan sonra içerideki yolcuların işlemi bitirilir.
- Her replikasyon bir "gün" olur ve günlük ortalamalar bağımsız gözlemler (Xⱼ) olarak kullanılır.

**Neden 1440 dk (1 gün)?**
- **Projede verilen varış parametresi** ("exponential, mean = 1.5 min"): Varış hızı gün içinde değişmeyen sabit bir hız olarak verilmiş (sabah/akşam yoğunluğu yok). Bu, tek bir uçuşun check-in penceresini değil, sürekli çalışan bir terminali tarif ediyor. Böyle bir sistemin doğal işletme döngüsü **bir gün**. Sonuçlar da "günlük performans" olarak yorumlanabiliyor.
- **Kısa süre yanıltıcı oluyor:** Simülasyon boş sistemle başlıyor. Süre kısa olursa bu boş başlangıç beklemeleri olduğundan düşük gösteriyor. Kararlı konfigürasyonları teorik (Erlang-C) değerle karşılaştırdık (30 replikasyon, ön deneme):

| Çalışma süresi | Check-in, 3 masa: ort. bekleme | Güvenlik, 4 tarayıcı: ort. bekleme |
|---|---|---|
| 180 dk (3 saat) | 5,4 dk | 2,3 dk |
| 480 dk (8 saat) | 7,7 dk | 3,2 dk |
| **1440 dk (1 gün)** | **8,5 dk** | **4,4 dk** |
| 2880 dk (2 gün) | 8,8 dk | 4,8 dk |
| Teorik uzun dönem (Erlang-C) | 9,6 dk | 4,9 dk |

  8 saatte check-in beklemesi teorik değerin yaklaşık %20 altında kalıyor. 1 günde fark yaklaşık %10'a iniyor. 2 güne çıkınca fark ancak %8 (check-in) ve %3'e (güvenlik) iniyor, ama "2 gün" gerçek bir işletme dönemine karşılık gelmiyor.
- **Kararsız konfigürasyonlarda** (2–3 tarayıcı) bekleme süresi çalışma süresiyle birlikte büyür (temel senaryoda güvenlik beklemesi 8 saatte ~33 dk, 1 günde ~91 dk). Bu bir hata değil, kapasitenin yetmediğinin göstergesi. Notebook'ta bunu küçük bir grafikle (çalışma süresi ↔ ortalama bekleme) göstermek iyi olur.
- Süre kodda tek parametre (`Config.OPEN_TIME`). Başka bir süre gerekirse tek satır değişir.

Bu karar ve gerekçesi notebook'ta açıkça yazılmalı. **Kararsızlık bulgusu sunumda güçlü bir nokta:** 2×2 deney, "3 tarayıcı yetmiyor, en az 4 gerekli" sonucunu sayılarla gösterecek.

---

## 3. Kavramsal model

**Varlıklar (entities):** Yolcular
**Kaynaklar (resources):** Check-in masaları (`simpy.Resource`, kapasite c), güvenlik tarayıcıları (`simpy.Resource`, kapasite s)
**Durum değişkenleri:** Qc (check-in kuyruğu), Sc (boş masa), Qs (güvenlik kuyruğu), Ss (boş tarayıcı)
**Gecikmeler:** {tA} varışlar arası süre, {tC} check-in hizmet süresi, {tS} güvenlik hizmet süresi

**Varsayımlar ve basitleştirmeler:**
- Tek, ortak FIFO kuyruğu (her istasyonda bir sıra, ilk boşalan masaya gidilir)
- Check-in ile güvenlik arasında yürüme süresi 0
- Herkes check-in yapar, kimse kuyruktan ayrılmaz
- Varış hızı gün içinde sabit
- Arıza yok, personel molası yok

### Event Graph (tandem kuyruk)

```
            tA
         ┌──────┐
         ▼      │
 Run ──► Arrival ──[Sc>0]──► StartCheckin ──tC──► EndCheckin ──[Qc>0]──► StartCheckin
 {Qc=0,Sc=c,                                          │
  Qs=0,Ss=s}                                          ▼ [Ss>0]
                                                StartSecurity ──tS──► EndSecurity ──[Qs>0]──► StartSecurity
```

Notebook'ta event graph çizimi (draw.io / Graphviz, `docs/event_graph/event_graph.png`) ve her olayın durum değişikliği tablosu yer alacak. Olaylar, kenarlar ve koşulların tam listesi `docs/event_graph/README.md` dosyasında.

---

## 4. Yöntem: neyi neden kullanıyoruz

Her adım ya proje metninin doğrudan bir isteğini karşılıyor ya da sonuçların doğru olduğunu göstermek için gerekli.

| Adım | Neden | Nasıl |
|---|---|---|
| Event Graph | Proje metni istiyor | Tandem kuyruk: Arrival → StartCheckin → EndCheckin → StartSecurity → EndSecurity |
| SimPy modeli | Proje metni istiyor | İki `simpy.Resource` (masalar, tarayıcılar), yolcu başına bir süreç, `Config` sınıfından parametreler |
| Zaman-ortalamalı metrikler, B(t), Q(t) | Proje metni istiyor | Kuyruk uzunluğu ve meşgul sunucu sayısı her `DT` dakikada bir kaydedilir. Ortalamalar ve grafikler bu kayıtlardan çıkar. |
| Terminating simülasyon, 1440 dk | Temel senaryo kararsız (Bölüm 2) | Varışlar 1440. dakikada durur, sistem boşalınca biter |
| Bağımsız replikasyonlar + t güven aralığı | Proje metni istiyor | Her replikasyonun ortalaması bir gözlem: X̄ ± t(n−1, 1−α/2)·√(S²/n) |
| β için replikasyon sayısı | Proje metni istiyor | n* = min{i ≥ n : t(i−1, 1−α/2)·√(S²/i) ≤ β}, sonra n* − n ek replikasyon |
| 2×2 faktöriyel deney | Proje metni istiyor (faktörler) | Masa {3,5} × tarayıcı {2,4} + temel (5,3). Ana etkiler ve etkileşim tablosu + grafik. |
| Erlang-C doğrulaması | Modelin doğru çalıştığını göstermek | Kararlı istasyonlarda simülasyon beklemesi teorik M/M/c değeriyle karşılaştırılır |
| Animasyon | ★ %10 bonus | `event_log` kaydını oynatan 2D matplotlib animasyonu |

---

## 5. Görev bölümü: 3 paralel hat + devir teslim

İş üç **hatta** ayrıldı. Üç hat aynı anda yürür. Her fazın sonunda herkes kendi hattını **devir notuyla** bir sonraki kişiye bırakır ve başka bir hattı, bir önceki kişinin kaldığı yerden devralır. Böylece:
- Herkes aynı anda çalışır, kimse kimseyi beklemez (hatlar arasındaki arayüzler iskelette baştan sabit).
- Her iş bir sonraki kişi tarafından kontrol edilip devam ettirilir. Herkes projenin her kısmına dokunur.

| Hat | Kapsam | Dosyalar | Notebook bölümleri |
|---|---|---|---|
| **A: Model** | SimPy modeli, Monitor, metrikler, B(t)/Q(t), doğrulama | `model.py`, `monitor.py`, `plots.py` | 4, 5 |
| **B: Analiz** | Replikasyon, güven aralığı, β, faktör deneyleri | `analysis.py` | 6, 7, 8 |
| **C: Tasarım ve animasyon** | Kavramsal model, Event Graph, ★ animasyon | `docs/event_graph/`, `animation.py` | 2, 3, 9 |

**Notebook bölümleri:** Tablodaki numaralar, teslim edilecek `notebooks/Airport_Checkin_Security.ipynb` iskeletindeki bölümler. Bölüm sırasını biz belirledik, hocanın istediği her maddeye bir bölüm düşecek şekilde (notebook İngilizce, başlıklar notebook'taki gibi):

| No | Bölüm | Hocanın hangi isteğini karşılıyor | Hat |
|---|---|---|---|
| 1 | Problem definition and objectives | Notebook'ta açıklama | Herkes (son gün) |
| 2 | Conceptual model (system, assumptions) | Tasarımın açıklanması | C |
| 3 | Event Graph | "Draw the Event Graph" | C |
| 4 | SimPy model | "Implement ... using python and SimPy" | A |
| 5 | Single-run outputs + B(t)/Q(t) | Ortalama gecikme, kalış süresi, zaman-ortalamalı sayılar, kullanım, B(t), Q(t), maks. kuyruk | A |
| 6 | Replications and confidence intervals | "Multiple replications ... confidence intervals" | B |
| 7 | Number of replications for β | "Best number of replications for an error margin β" | B |
| 8 | Factor experiments (2×2) | "Investigate the impact of selected factors" | B |
| 9 | Animation (10% bonus) | ★ %10 bonus | C |
| 10 | Conclusions, assumptions, limitations | Notebook'ta açıklama | Herkes (son gün) |

**Sabit arayüzler** (paralel çalışmayı mümkün kılan şey, değiştirmeden önce herkese haber verin):
`run_simulation(config, seed) -> RunResult`, `RunResult` alanları, `event_log` olay adları (`ARRIVAL`, `START_CHECKIN`, `END_CHECKIN`, `START_SECURITY`, `DEPARTURE`), `METRIC_KEYS`.

### Faz 1 (27 Kasım – 2 Aralık): temeller

| Kişi | Hat | Yapılacak | Faz sonunda teslim edilen |
|---|---|---|---|
| Burkay | A | Temel SimPy modeli: varış → check-in → güvenlik, 1440 dk sonra varış durur, sistem boşalınca biter. `PassengerRecord`, `event_log` doldurulur. `summarize` en az gecikme ve sistemde kalış sürelerini hesaplar. | `run_simulation()` çalışıyor, tek çalıştırmanın çıktısı yazdırılabiliyor |
| Nisa | B | `confidence_interval`, `required_replications` (iteratif n* formülü), `replicate`, `run_experiments`. Model hazır olmadığı için **sahte veriyle** (ör. rastgele sayılar) test edilir. | Fonksiyonlar sahte veriyle doğru sonuç veriyor, birim testleri var |
| Ceren | C | Kavramsal model (varlıklar, kaynaklar, durum değişkenleri, varsayımlar), Event Graph çizimi, olayların durum değişikliği tablosu, notebook Bölüm 2–3 metni | `event_graph.png` + Bölüm 2–3 dolu |

### Devir 1 (2 Aralık)
- Burkay → **Ceren**'e A hattını devreder. (Ceren event graph'ı çizdiği için modelin olaylarla birebir aynı olup olmadığını en iyi o kontrol eder.)
- Nisa → **Burkay**'a B hattını devreder. (Burkay modeli yazdığı için analiz fonksiyonlarını gerçek modele en hızlı o bağlar.)
- Ceren → **Nisa**'ya C hattını devreder.

### Faz 2 (3 – 8 Aralık): tam metrikler ve gerçek sonuçlar

| Kişi | Hat | Yapılacak | Faz sonunda teslim edilen |
|---|---|---|---|
| Ceren | A | Modeli event graph ile karşılaştır, `Monitor` (her `DT`'de Qc, Qs, Bc, Bs örneği), zaman-ortalamalı metrikler, kullanım oranları, maks. kuyruk uzunluğu, B(t)/Q(t) grafikleri | `summarize()` 10 metriğin hepsini veriyor, grafikler çiziliyor |
| Burkay | B | Analiz fonksiyonlarını gerçek modele bağla. Temel senaryo: n₀ = 10 replikasyon, iki kuyruk için %95 güven aralığı, β için n*, n* replikasyonla güncellenmiş aralıklar | Bölüm 6–7 sonuçları (tablo) |
| Nisa | C | ★ Animasyonun ilk çalışan sürümü: `event_log`'u oynatan matplotlib animasyonu (masalar, tarayıcılar, kuyruklar, saat) | İlk GIF |

### Devir 2 (8 Aralık)
- Ceren → **Nisa**'ya A hattını devreder.
- Burkay → **Ceren**'e B hattını devreder.
- Nisa → **Burkay**'a C hattını devreder.

### Faz 3 (9 – 14 Aralık): doğrulama, deneyler, bitirme

| Kişi | Hat | Yapılacak | Faz sonunda teslim edilen |
|---|---|---|---|
| Nisa | A | Doğrulama: 5 masalı check-in ve 4 tarayıcılı güvenlik sonuçlarını Erlang-C teorik değerleriyle karşılaştır. Çalışma süresi ↔ ortalama bekleme grafiği (kararsızlığı gösterir). Kod yorumları ve temizlik. | Bölüm 4–5 son hali |
| Ceren | B | 2×2 faktör deneyi (masa {3,5} × tarayıcı {2,4}) + temel senaryo, sonuç tablosu, ana etki / etkileşim grafikleri, yorum | Bölüm 8 son hali |
| Burkay | C | ★ Animasyonu bitir (görsel düzen, hız, GIF/MP4), notebook Bölüm 9 | Bitmiş animasyon |

### Son (15 – 16 Aralık): birlikte bitirme
Herkes birlikte: Bölüm 1 (amaç) ve 10 (sonuçlar, varsayımlar, kısıtlar), kodu notebook'a gömme, "Restart & Run All", planın sonundaki kontrol listesi, **16 Aralık teslim**.

### Devir notu (her devirde zorunlu)
Devreden kişi `docs/handoff/TEMPLATE.md` şablonunu kopyalayıp `docs/handoff/<hat>-phase<N>.md` (ör. `A-phase1.md`) dosyasını İngilizce doldurur ve hattının dalını PR olarak açar. **Devralan kişi PR'ı inceleyip birleştirir.** Devir böylece aynı zamanda kod incelemesi olur. Şablonun başlıkları:

```markdown
# Handoff: Lane <A/B/C>, Phase <N>  (<from> → <to>)
## Done                                  (bitenler)
## Where (file / function / notebook section)
## How to run (command or cell)
## What I checked and results            (neyi kontrol ettim, ne çıktı)
## Unfinished / TODO (by priority)       (yarım kalanlar)
## Watch out / known issues              (dikkat edilecekler)
```

İş yükü: herkes her hatta bir faz çalışıyor, bu yüzden toplam yük eşit. Fazlar arasında takılan biri olursa devir tarihi değişmez: yarım kalan iş TODO olarak devredilir.

---

## 6. Çalışma düzeni (GitHub)

- Her hat için bir dal: `lane-a/model`, `lane-b/analysis`, `lane-c/design`. Dal kişiye değil hatta ait, devralan kişi aynı dalda devam eder.
- Devirde PR açılır, devralan kişi inceleyip `main`'e birleştirir, sonra yeni fazda dalı `main`'den günceller.
- Kod `src/airport_sim/` içinde geliştirilir, notebook bunları içe aktarır. Hoca tek bir notebook istediği için son gün kod notebook'a gömülür.
- Notebook'ta merge çakışması çok olur: herkes kendi bölümünü `notebooks/drafts/lane-<x>.ipynb` içinde hazırlar, ana notebook'a son gün birleştirilir.
- Sonuçlar tekrarlanabilir olmalı: her replikasyonda `seed = RANDOM_SEED + r`.
- Dil: PLAN.md Türkçe, GitHub'daki diğer her şey İngilizce (kod, yorumlar, notebook, dokümanlar, commit mesajları, PR'lar).

---

## 7. Bitmiş sayılma kriterleri (teslimden önce kontrol listesi)

- [ ] Event graph notebook'ta görünüyor ve SimPy koduyla birebir aynı olayları içeriyor
- [ ] Bütün zorunlu metrikler **her iki** kuyruk/istasyon için var
- [ ] B(t) ve Q(t) grafikleri her istasyon/kuyruk için var
- [ ] Maksimum kuyruk uzunluğu raporlandı
- [ ] n₀ replikasyonla %95 güven aralıkları, β için n*, n* replikasyonla güncellenmiş güven aralıkları var
- [ ] 2×2 deney tablosu ve yorumu var
- [ ] Varsayımlar, kısıtlar ve terminating kararının gerekçesi yazıldı
- [ ] Notebook "Restart & Run All" ile hatasız çalışıyor
- [ ] ★ Animasyon (kesin yapılacak) bitti, notebook'ta ve demoda gösterilebilir
