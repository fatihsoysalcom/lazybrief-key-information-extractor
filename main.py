import re

def generate_lazybrief(full_text: str) -> str:
    """
    Generates a 'Lazybrief' (concise summary) from a longer text.
    This simulates distilling key information to save the reader's time.
    """
    # Split the text into sentences using common punctuation marks.
    # The regex uses a positive lookbehind to keep the punctuation with the sentence.
    sentences = re.split(r'(?<=[.!?])\s+', full_text)

    brief_parts = []

    # --- Lazybrief Principle 1: High-level Overview (Minimum Effort for Reader) ---
    # Start with the most crucial information immediately to provide quick context.
    if sentences:
        brief_parts.append("--- Lazybrief: Hızlı Özet ---")
        brief_parts.append("\n**Ana Konu:**")
        # Take the first sentence as a very quick overview
        brief_parts.append(sentences[0].strip())
        if len(sentences) > 1:
            # Add a second sentence for slightly more context if available
            brief_parts.append(sentences[1].strip())

    # --- Lazybrief Principle 2: Key Takeaways & Action Items (Distilling Essence) ---
    # Identify sentences that contain action-oriented keywords or critical information.
    # These are the "must-know" points, removing unnecessary details from the original text.
    action_keywords = [
        "gerekir", "gerekmektedir", "acilen", "tamamlamalıdır", "sunulacak",
        "devreye alınacak", "deadline", "önemli", "karar", "hedef", "aksiyon",
        "bir sonraki adım", "çözmesi gerekiyor", "iletişim kurulmalı", "planlanmalı"
    ]
    key_points = []
    for i, sentence in enumerate(sentences):
        # Skip the first two sentences as they are already included in the overview
        if i < 2:
            continue
        # Check for keywords (case-insensitive) to identify critical information.
        if any(keyword in sentence.lower() for keyword in action_keywords):
            key_points.append(sentence.strip())

    if key_points:
        brief_parts.append("\n**Önemli Kararlar & Aksiyon Adımları:**")
        for point in key_points:
            brief_parts.append(f"- {point}")
    else:
        brief_parts.append("\n**Önemli Kararlar & Aksiyon Adımları:** Belirlenen önemli aksiyon adımı bulunamadı.")


    # --- Lazybrief Principle 3: Conciseness & Efficiency ---
    # End with a clear indication that the brief is complete, encouraging quick consumption
    # and directing to the full text for deeper understanding if needed.
    brief_parts.append("\n--- Daha Fazla Detay İçin Orijinal Metne Bakınız ---")

    return "\n".join(brief_parts)

# --- Example Usage ---
# Simulate a long email, meeting notes, or a report that needs summarization.
long_text_example = """
Bugünkü toplantımızda, Q3 satış hedeflerini ve pazarlama stratejilerini derinlemesine ele aldık. Satış ekibi, mevcut performansın beklentilerin altında olduğunu ve özellikle yeni ürün lansmanının gecikmesi ile rakip firmanın agresif fiyatlandırma politikasının ana etkenler olduğunu belirtti. Bu durumun detaylı analizi için bir sonraki hafta özel bir oturum düzenlenecektir. Bu oturumda, pazar payı analizleri ve müşteri segmentasyonu konuları da ele alınacaktır.

Pazarlama departmanı, sosyal medya kampanyalarının etkisini artırmak için yeni bir içerik planı sunacak. Bu planın detayları gelecek hafta Salı günü paylaşılacak ve tüm paydaşların geri bildirimleri alınacaktır. Ayrıca, müşteri geri bildirimlerini toplamak için yeni bir anket sistemi devreye alınacak. Bu anketin sonuçları, ürün geliştirme ekibine iletilecek ve ürün yol haritasında dikkate alınacaktır. Yeni ürün geliştirme süreçlerinin hızlandırılması da planlanmalı.

Bir sonraki toplantımızda, satış hedeflerine ulaşmak için revize edilmiş bir eylem planı sunulması gerekmektedir. Bu planın, mevcut pazar koşulları ve rakip analizleri ışığında hazırlanması önemlidir. Tüm ekiplerin bu konularda işbirliği yapması gerektiği vurgulandı. Özellikle Mehmet Bey'in yeni ürün lansmanı gecikmesi ile ilgili durumu acilen çözmesi gerekiyor. Ayşe Hanım ise sosyal medya kampanya planını Pazartesi'ye kadar tamamlamalıdır. Deadline: Cuma günü, revize edilmiş eylem planı sunulmalıdır. Ayrıca, potansiyel iş ortaklarıyla iletişim kurulmalı ve yeni iş geliştirme fırsatları araştırılmalıdır. Gelecek ay için bütçe revizyonu da planlanmalı ve ilgili departmanlara bildirilmelidir.
"""

if __name__ == "__main__":
    print("--- Orijinal Metin ---")
    print(long_text_example)
    print("\n" + "="*50 + "\n")

    lazy_brief_output = generate_lazybrief(long_text_example)

    print("--- Lazybrief Çıktısı ---")
    print(lazy_brief_output)
