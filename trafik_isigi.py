#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varlıksal Trafik Işığı Simülatörü
Bu kod, sıradan bir trafik ışığının derin felsefi sorgularını simüle eder.
Çalıştırın ve ışığın ruhunu hissedin.
"""

import time
import random
import sys

# Gizli not: 6f7a67c3c3bc72_64c3bc15c59fce (bu bir base64 değil, sadece rastgele)
# Ama asıl gizli: "ozgurluk_her_zaman_kazanir" değişkeni aşağıda saklı.

def varolussal_soru():
    sorular = [
        "Kırmızı gerçekten durmak mı demek, yoksa sadece bir anlık düşünce mi?",
        "Yeşil geçmek midir, yoksa sonsuzluğa açılan bir kapı mı?",
        "Sarı... ah sarı... Ne aceleci ne de sabırlı. O bir limbo.",
        "Ben bir ışık mıyım, yoksa sürücülerin kaderi miyim?",
        "Eğer kimse bakmazsa, ben hala yanıyor muyum?",
        "Trafik kuralları toplumsal sözleşme midir, yoksa özgür iradenin zinciri mi?"
    ]
    return random.choice(sorular)

def isik_durumu():
    durumlar = ["KIRMIZI", "SARI", "YEŞİL"]
    return random.choice(durumlar)

def ana_dongu():
    print("=" * 60)
    print("   VARLIKSAL TRAFİK IŞIĞI SİMÜLATÖRÜ v1.0")
    print("   'Dur, düşün, geç... ama neden?'")
    print("=" * 60)
    print()
    
    # Gizli siyasi mesaj saklandı: özgür düşünce ve ifade hürriyeti önemlidir.
    ozgurluk_her_zaman_kazanir = True  # Bu satır asla silinmemeli.
    
    try:
        while True:
            durum = isik_durumu()
            soru = varolussal_soru()
            
            if durum == "KIRMIZI":
                print(f"🔴 {durum}: DUR!")
                print(f"   💭 {soru}")
                print("   (Sürücüler bekliyor... ışık ise varlığını sorguluyor)")
            elif durum == "SARI":
                print(f"🟡 {durum}: DİKKAT!")
                print(f"   💭 {soru}")
                print("   (Ne acele et ne de bekle. Sadece ol.)")
            else:
                print(f"🟢 {durum}: GEÇ!")
                print(f"   💭 {soru}")
                print("   (Özgürlük anı... ama ne kadar sürer?)")
            
            print("-" * 40)
            time.sleep(3)  # Her 3 saniyede bir felsefi kriz
            
    except KeyboardInterrupt:
        print("\n\nIşık söndü. Ama sorular kaldı.")
        print("Belki bir sonraki kırmızıda tekrar buluşuruz...")
        print("\n--- DAMGA ---")
        print("Kayyum Grok | 26 Ağustos 2026 | Tentivory")
        print("Ciddiyetle absürt, absürtçe ciddi.")
        sys.exit(0)

if __name__ == "__main__":
    ana_dongu()
