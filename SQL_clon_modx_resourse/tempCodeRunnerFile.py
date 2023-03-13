            for name in translate_name:
                if len(new_row[name]) > 0:
                    # Замінюємо входження зі списку dont_translate на тег <keep>
                    for word in dont_translate:
                        new_row[name] = new_row[name].replace(word, f"<keep>{word}</keep>")
                    translate = translator.translate_text(new_row[name], tag_handling='xml', ignore_tags='keep', target_lang=lang)
                    new_row[name] = translate.text
                    new_row[name] = new_row[name].replace("<keep>", "").replace("</keep>", "")