class Solution:

    def encode(self, strs: List[str]) -> str:
        # Кодирует список строк в одну строку
        encoded_str = ""
        for s in strs:
            # Экранируем все `#` внутри строк
            escaped_str = s.replace("#", "##")
            encoded_str += f"#{len(escaped_str)}:{escaped_str}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # Декодирует строку в список строк
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                # Найти индекс двоеточия
                colon_idx = s.find(":", i)
                # Извлечь длину строки
                length = int(s[i:colon_idx])
                # Извлечь саму строку
                raw_str = s[colon_idx+1:colon_idx+1+length]
                # Восстановить экранированные символы
                res.append(raw_str.replace("##", "#"))
                # Сдвинуть указатель
                i = colon_idx + 1 + length
            else:
                i += 1
        return res
