import numpy as np

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum()

mahalleler = ["Güzel Mahallesi", "DahaGüzel Mahallesi", "Kloroplast Mahallesi"]
veri = {
    "Güzel Mahallesi": {
        "Nüfus yoğunluğu": 800,
        "Mevcut ulaşım altyapısı": 3,
        "Maliyet analizi": -500000,
        "Çevresel etki": 2,
        "Sosyal fayda": 90
    },
    "DahaGüzel Mahallesi": {
        "Nüfus yoğunluğu": 1200,
        "Mevcut ulaşım altyapısı": 4,
        "Maliyet analizi": -700000,
        "Çevresel etki": 3,
        "Sosyal fayda": 85
    },
    "Kloroplast Mahallesi": {
        "Nüfus yoğunluğu": 1000,
        "Mevcut ulaşım altyapısı": 2,
        "Maliyet analizi": -600000,
        "Çevresel etki": 4,
        "Sosyal fayda": 95
    }
}
kriterler = ["Nüfus yoğunluğu",
             "Mevcut ulaşım altyapısı",
             "Maliyet analizi",
             "Çevresel etki",
             "Sosyal fayda"]

best_weights = {
    "Nüfus yoğunluğu": 0.3,
    "Mevcut ulaşım altyapısı": 0.2,
    "Maliyet analizi": 0.1,
    "Çevresel etki": 0.15,
    "Sosyal fayda": 0.25
}

final_skorlar = {}
for mahalle in mahalleler:
    toplam_skor = sum(veri[mahalle][kriter] * best_weights[kriter] for kriter in kriterler)
    final_skorlar[mahalle] = toplam_skor

final_values = np.array(list(final_skorlar.values()))
softmax_skorlar = softmax(final_values)
best_mahalle = mahalleler[np.argmax(softmax_skorlar)]

print("Mahalle kriter değerleri:")
for mahalle in mahalleler:
    kriter_degerleri = ", ".join([f"{kriter}: {veri[mahalle][kriter]}" for kriter in kriterler])
    print(f"{mahalle} ({kriter_degerleri})")

print("\nEn iyi ağırlık değeri:")
for kriter, weight in best_weights.items():
    print(f"{kriter}: {weight:.3f}")

print("\nMahalleler için hesaplanan skorlar:")
for mahalle, skor in zip(mahalleler, softmax_skorlar):
    print(f"{mahalle}: {skor:.3f}")

print(f"\nEn uygun güzergah: {best_mahalle}")