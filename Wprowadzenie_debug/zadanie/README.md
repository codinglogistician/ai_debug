---


# 📝 Zadanie: Postawienie drugiego Gradio z mniejszym Whisperem

Uruchom usługę `gradio-whisper` z modelem **Whisper Small**.

---

## 1. Zmodyfikuj `app.py`

Zmodyfikuj plik `app.py`, z pipeline dla mniejszego modelu Whisper Tiny.


---

## 2. Zbuduj i uruchom obraz 

```bash
docker build -t gradio-whisper .
```

# uruchomienie
```
docker run -d --name gradio-whisper -p 8000:8000 gradio-whisper:latest
```

---

## 3. Przetestuj w przeglądarce przez guacamole lub przez forwarding portu

* Whisper Tiny → [http://localhost:8000](http://localhost:8000)

---

## 4. Test

1. Wgraj ten sam plik audio do obu interfejsów:

   * zmierz czas transkrypcji,
   * porównaj dokładność wyników.

2. W terminalu użyj:

   ```bash
   docker stats
   ```

   Sprawdź:

   * zużycie CPU/RAM przez Whisper Tiny.

---

