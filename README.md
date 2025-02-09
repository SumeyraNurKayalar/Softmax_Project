İlk olarak kodun başında matematiksel işlemler yapacağımız için numpy paketi import edilir.
Softmax fonksiyonu kullanılan değerleri normalize ederek her değerin topplamdan olan oranını hesaplar.
Bu veri toplamlarının 1'e eşit olması sağlanır.
def softmax(x): ile softmax fonksiyonu tanımlanır, x parameresi fonksiyon içine tanımlanarak bu değerin hesaplarda kullanılması sağlanır.
exp_x = np.exp(x - np.max(x)) kodu ile x'ten en büyük değer çıkarılır ve sayısal kararsızlık önlenir.
return exp_x / exp_x.sum() kodu ile değerler toplamı 1 olacak şekilde normalizasyon yapılır. Mahallelerin kriterlere dayalı hesaplanan toplam skorları normalize eder.
mahalleler =  kısmında mahalle iimleri tanımlanır.
veri =  kısmında her mahalle için istenen kriterler ve bu kriterlerin değerleri gösterilir.
kriterler =  kısmında bu kriter isimleri tanımlanır.
best_weights = bu kodda her kriter için girilen ağırlık bulunur. Bu ağırlıklar her kriterin karar vermede ne kadar etkili olacağını belirler.
final_skorlar kodunda temelde her mahalle için kriterlere dayalı toplam bir skor hesaplanır.
for mahalle in mahalleler:  ile bu for döngüsünün her mahalle için çalışması sağlanır.
toplam_skor = sum(veri[mahalle][kriter] * best_weights[kriter] for kriter in kriterler) burada ilk mahallenin kriter değeri alınır ve kriter ağırlığıyla çarpılır ve sum içerisinde tüm kriterler için çarpılan değerler toplaır.
final_skorlar[mahalle] = toplam_skor bu kısım toplam skor değerinin tutulduğu yerdir.
final_values = np.array(list(final_skorlar.values())) ile np.array içindeki skorlar numpy dizisine dönüştürülür.
softmax_skorlar = softmax(final_values) ile mahalle skorlarına softmax fonksiyonu uygulanır. Burada gerekli matematiksel işlemler softmax fonksiyonnuyla sağlanır.
Yapılan işlemler sonucu en yüksek skorlu mahalle en yüksek softmax değerine de sahip olur en iyi mahalle olarak alınır.
best_mahalle = mahalleler[np.argmax(softmax_skorlar)] ile her mahalle .için hesaplanan kriter değerleri, en iyi ağırlık değeri, softmax skorları ve en iyi mahallenin ismi yazdırılır.
Burada np.argmax içindeki softmax_skorlar ifadesinin en yüksek indeksini bulur.
Mahalle kriter değerini veren print için kullanılan for döngüsü mahalleler listesindeki her mahalle için çalışır.
kriter_degerleri = ", ".join([f"{kriter}: {veri[mahalle][kriter]}" for kriter in kriterler]) kısmıında kriterler listesindeki her kriter için veriden kriter değeri alınır ve kriterin değerlerini verecek bir liste oluşturulur.
join ile bu liste elemmanları tek bir String haline getirilir.
En iyi ağırlığı veren print için kullanılan for, for kriter, weight in best_weights.items(): şeklinde best_weights kısmından her kriter ve ağırlık değerini alır.
items() metoduyla kriter ve değer çiftleri döndürülür. Sonrasında ağırlık değeri üç ondalık basamaklı olacak şekilde terminale yazdırılır.
Mahalle skorlarını gösteren print için zip içindeki mahalleler ve softmax_skorlar listelerini eşleştirip her mahalle için döngü tekrar çalıştırılır.
Daha sonra tekrardan aynı şekilde yazdırılacak olan değer üç ondalıklı bir şekilde yazdırılır.
En son kısımda print(f"\nEn uygun güzergah: {best_mahalle}") kodunda en uygun güzergah yazdırılır ve en yüksek softmax değeri olan mahalle ismi {best_mahalle} ile terminale yazdırılır.
