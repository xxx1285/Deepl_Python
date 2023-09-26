map_TIR2_comments = {
    # "https://tr.infonorthcyprus.com": {
    #     "urls": [
    #         "/post",
    #         "/water",
    #         "/electricity"
    #     ],
    #     "selenium_actions": []
    # },
    "https://blogs.cornell.edu": {
        "urls": [
            "/advancedrevenuemanagement12/2012/03/28/revenue-management-in-the-golf-industry/comment-page-223/",
            "/advancedrevenuemanagement12/2012/03/28/tennis-center-revenue-management/",
            "/advancedrevenuemanagement12/2012/03/28/a-revenue-managers-point-of-view-on-hospitals/",
            "/advancedrevenuemanagement12/2012/03/28/casino-revenue-management/",
            "/advancedrevenuemanagement12/2012/03/28/sports-stadium-rm/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="wp-comment-cookies-consent"]').click()""",
            """captcha_img_XPATH = '//*[@id="secureimg"]'""",                                            # XPATH images
            """captcha_img_XPATH_text = fun_my_captcha_image(driver, captcha_img_XPATH)""",
            """captcha_find_input_text = driver.find_element(By.XPATH, '//*[@id="securitycode"]')""",    # XPATH поле ввода
            """ActionChains(driver).move_to_element(captcha_find_input_text).click().perform()""",
            """captcha_find_input_text.send_keys(captcha_img_XPATH_text)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()""",
        ]
    },
    "https://www.teny.gr": {
        "urls": [
            "/journal3/blog/post?journal_blog_post_id=1"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a7 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').click()""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()""",
        ]
    },
    "https://www.leadsister.com": {
        "urls": [
            "/index.php?route=journal3/blog/post&journal_blog_post_id=10",
            "/index.php?route=journal3/blog/post&journal_blog_post_id=11",
            "/index.php?route=journal3/blog/post&journal_blog_post_id=7",
            "/index.php?route=journal3/blog/post&journal_blog_post_id=9",
            "/index.php?route=journal3/blog/post&journal_blog_post_id=3"
        ],
        "selenium_actions": [
            """a3 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a5 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a7 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').click()""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a10 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()""",
        ]
    },
    "https://rushbiz.ru": {
        "urls": [
            "/upravlenie-biznesom/buxuchet/raschet-effektivnosti-biznesa/stroka-v-balanse.html",
            "/upravlenie-biznesom/buxuchet/raschet-effektivnosti-biznesa/operacionnaya-pribyl.html",
            "/upravlenie-biznesom/buxuchet/raschet-effektivnosti-biznesa/koefficient-oborachivaemosti-aktivov.html",
            "/upravlenie-biznesom/buxuchet/raschet-effektivnosti-biznesa/porog-rentabelnosti-formula.html",
            "/upravlenie-biznesom/buxuchet/raschet-effektivnosti-biznesa/raschet-rentabelnosti-prodazh.html"
        ],
        "selenium_actions": []
    },
    "https://www.housans.com": {
        "urls": [
            "/index.php?route=information/blogger&blogger_id=12",
            "/index.php?route=information/blogger&blogger_id=13",
            "/index.php?route=information/blogger&blogger_id=11"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-author"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a7 = driver.find_element(By.XPATH, '//*[@id="add-comment"]/form/div[4]/input').click()"""
        ]
    },
    "https://kulo.dk": {
        "urls": [
            "/blog/journal-blog",
            "/blog/vacation-time",
            "/blog/best-leather-bags",
            "/blog/another-blog-post",
            "/blog/greece-travel",
            "/blog/season-essentials",
            "/blog/classic-watches",
            "/blog/wool-jackets"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()"""
        ]
    },
    "https://yfosbags.com": {
        "urls": [
            "/journal-blog",
            "/season-essentials",
            "/best-beauty-products",
            "/classic-watches",
            "/wool-jackets",
            "/greece-travel",
            "/best-leather-bags",
            "/another-blog-post",
            "/vacation-time"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()"""
        ]
    },
    "https://classico.bg": {
        "urls": [
            "/another-blog-post",
            "/best-leather-bags",
            "/journal-blog",
            "/season-essentials",
            "/best-beauty-products",
            "/classic-watches",
            "/wool-jackets",
            "/vacation-time",
            "/greece-travel"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()"""
        ]
    },
    "https://loomfresh.com": {
        "urls": [
            "/blog/journal-blog-is-here",
            "/blog/best-leather-bags",
            "/blog/another-blog-post",
            "/blog/greece-travel",
            "/blog/journal-blog",
            "/blog/season-essentials",
            "/blog/best-beauty-products",
            "/blog/classic-watches",
            "/blog/wool-jackets"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()"""
        ]
    },
    "https://www.apotekavalerijana.rs": {
        "urls": [
            "/savetovaliste/kako-zaustaviti-opadanje-kose",
            "/savetovaliste/secer-i-holesterol-postoji-li-veza",
            "/savetovaliste/pet-saveta-za-muskarce-kako-do-lepse-koze-lica",
            "/savetovaliste/deset-nacina-kako-da-sprecite-pojavu-akni",
            "/savetovaliste/carobni-stapic-za-kozu",
            "/savetovaliste/kako-se-izboriti-sa-kandidom",
            "/savetovaliste/hronicno-ste-umorni"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()"""
        ]
    },
    "https://www.myangadi.com": {
        "urls": [
            "/blog/journal-blog-is-here",
            "/blog/best-leather-bags",
            "/blog/another-blog-post",
            "/blog/greece-travel",
            "/blog/season-essentials",
            "/blog/best-beauty-products",
            "/blog/classic-watches",
            "/blog/wool-jackets"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()"""
        ]
    },
    "https://www.customringjewelry.com": {
        "urls": [
            "/custom-jewelry-ring-blog/how-do-i-get-a-custom-ring",
            "/custom-jewelry-ring-blog/the-best-jewelry-at-the-critics-choice-awards",
            "/custom-jewelry-ring-blog/how-to-select-jewel-ring",
            "/custom-jewelry-ring-blog/pros-and-cons-of-custom-jewelry",
            "/custom-jewelry-ring-blog/the-10-best-jewelry-brands-for-men",
            "/custom-jewelry-ring-blog/how-to-protect-your-freemason-ring",
            "/custom-jewelry-ring-blog/tips-to-consider-when-designing-your-custom-jewelry",
            "/custom-jewelry-ring-blog/4-types-of-bracelets-for-men"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="input-name"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="input-website"]').send_keys(www)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="input-comment"]').send_keys(comment)""",
            """a9 = driver.find_element(By.CLASS_NAME, 'comment-submit').click()"""
        ]
    },
    "http://son-et-lumiere.cowblog.fr": {
        "urls": [
            "/a-girl-named-elastika-3266667.html",
            "/anahit-giacinto-scelsi-3267527.html",
            "/kim-doo-soo-3266915.html",
            "/c-est-la-que-finit-la-mer-3184522.html",
            "/les-aurores-boreales-3165537.html",
            "/silence-absence-10-3125543.html",
            "/petites-planetes-3115664.html",
            "/prose-spontanee-3155797.html",
            "/trace-l-inegale-palindrome-3103054.html",
            "/voeu-3096446.html",
            "/marmonneur-de-mots-3091155.html",
            "/sans-les-mots-3266448.html"
        ],
        "selenium_actions": [
            """a3 = driver.find_element(By.XPATH, '//*[@id="auth-box"]/label[1]/input').send_keys(name)""",
            """a5 = driver.find_element(By.XPATH, '//*[@id="auth-box"]/label[2]/input').send_keys(name)""",
            """a7 = driver.find_element(By.XPATH, '//*[@id="comment-post"]/div/div[3]/label[1]/input').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="comment-post"]/div/div[3]/label[2]/input').send_keys(email)""",
            """a11 = driver.find_element(By.XPATH, '//*[@id="comment_content"]').send_keys(comment)""",
            """a12 = driver.find_element(By.XPATH, '//*[@id="comment-post"]/div/div[3]/label[3]/input').click()""",
            """a13 = driver.find_element(By.XPATH, '//*[@id="comment-post"]/div/div[3]/label[4]/input').click()""",
            """a14 = driver.find_element(By.XPATH, '//*[@id="commentsub"]').click()"""
        ]
    },
    "https://www.telugubulletin.com": {
        "urls": [
            "/tamil-heroine-divya-bharathi-bikini-new-pics-19279",
            "/akhil-akkinenis-agent-movie-launch-125424",
            "/prabhass-adipurush-muhurtham-photos-113370",
            "/photos-ram-charan-and-upasana-enjoy-in-us-trip-177689",
            "/hero-dharma-mahesh-latest-photoshoot-176021",
            "/photos-ram-charan-at-gma-show-in-usa-176959",
            "/pragya-jaiswal-photos-2-173603",
            "/mrunal-thakur-glam-pics-173597",
            "/thamanna-hot-photos-172066",
            "/ketika-sharma-glamour-pics-172021",
            "/sunny-leone-glamour-pics-2-172009"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="wp-comment-cookies-consent"]').click()""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://ubaxxi.uba.ar": {
        "urls": [
            "/inscripciones-a-la-uba-pre-ingreso/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="comment-submit"]').click()"""
        ]
    },
    "https://www.walf-groupe.com": {
        "urls": [
            "/tabaski-2022-en-deux-dates/",
            "/qatar-senegal-a-13h00-gmt-malheur-au-vaincu/",
            "/whatsapp-une-panne-mondiale-des-excuses-de-meta-et-des-questions/",
            "/kabirou-mbodje-symbole-senegalais-de-la-haine-de-soi/",
            "/kalifone-condamne-a-un-6-mois-dont-1-mois-ferme/",
            "/moustapha-diakhate-aminata-toure-viole-larticle-25-de-la-constitution/",
            "/le-liberal-amadou-ba-a-toujours-confondu-leconomie-et-la-mendicite-internationale-selon-mamadou-lamine-diallo/",
            "/nettoiement-trois-milliards-pour-mettre-fin-a-la-greve/",
            "/deficit-de-45-mille-enseignants-le-ministere-de-leducation-nationale-sexplique/",
            "/marche-ce-vendredi-pour-la-liberation-de-detenus-politiques/",
            "/bougane-gueye-contre-une-amnistie-calculee-de-karim-et-khalifa/",
            "/assemblee-nationale-mimi-demissionne-benno-perd-la-majorite/",
            "/francois-gomis-sg-du-syndicat-des-aiguilleurs-du-ciel-tous-les-vols-commerciaux-seront-affectes/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()""",
        ]
    },
    # "https://unravellingmag.com": {
    #     "urls": [
    #         "/articles/chinese-pidgin-english/",
    #         "/articles/the-aslian-languages/",
    #         "/articles/documenting-temiar/",
    #         "/articles/jahai/",
    #         "/articles/reduplication-in-austronesian-languages/",
    #         "/articles/orphaned-by-my-mothers-tongue/",
    #         "/articles/learning-tok-pisin/",
    #         "/articles/an-interview-with-hafiz-rashid/",
    #         "/articles/not-your-typical-type/",
    #         "/articles/naxi/",
    #         "/articles/cantonese/",
    #         "/articles/the-language-of-food-in-singapore/",
    #         "/articles/editors-foreword-13/"
    #     ],
    #     "selenium_actions": []
    # },
    "https://www.cufflinksgifthub.co.uk": {
        "urls": [
            "/cufflinks/reasons-collect-vintage-cufflinks/",
            "/cufflinks/custom-design-cufflinks/",
            "/exclusive-cufflinks/mens-dinosaur-cufflinks/",
            "/cufflinks/three-reasons-you-need-cufflinks-more-than-you-think/",
            "/cufflinks/brief-history-favourite-accessory-cufflink/",
            "/cufflinks/wedding-cufflinks/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()""",
        ]
    },
    "https://www.trails-endurance.com": {
        "urls": [
            "/a-la-une/3-nouvelles-courses-by-utmb",
            "/actus-trail/miut-2022-j-walmsley-et-c-dauwalter-au-dessus-du-lot",
            "/coureurs-trail-running/teams-trails-running-france-2022",
            "/coureurs-trail-running/record-24h-d-d-objectif-18-000-m",
            "/actus-trail/western-states-et-de-3-pour-j-walmsley",
            "/actus-trail/record-du-monde-denivele-en-24-h",
            "/actus-trail/sebastien-raichon-boucle-le-gr5-en-autonomie-complete-en-162h09",
            "/coureurs-trail-running/integre-le-team-trailhero-dynafit"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://www.filosofico.net": {
        "urls": [
            "/diegofusaro/curiosita/",
            "/diegofusaro/foto/",
            "/diegofusaro/il-pensiero/"
        ],
        "selenium_actions": [
            """time.sleep(2)""",
            """iframe_element = driver.find_element(By.XPATH, "//iframe[contains(@style, 'position: fixed')]")""",
            """driver.switch_to.frame(iframe_element)""",
            """button_element = driver.find_element(By.XPATH, "//span[text()='Accetta e Chiudi']").click()""",
            """driver.switch_to.default_content()""",
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://www.zoology.ubc.ca": {
        "urls": [
            "/~turner/Crossflower/2016/09/15/the-beginning/",
            "/~turner/Crossflower/2016/09/15/hallo-tubingen/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="wp-comment-cookies-consent"]').click()""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://conferences.law.stanford.edu": {
        "urls": [
            "/ipsummerschool2022/2014/01/21/porta-est-nascetur-proin-2/",
            "/ipsummerschool2022/2014/01/21/et-auctor-tortor-nunc-2/",
            "/ipsummerschool2022/2014/01/21/purus-rhoncus-et-lundium-2/",
            "/ipsummerschool2022/2014/01/21/ac-pulvinar-turpis-scelerisque-2/",
            "/ipsummerschool2022/2013/12/29/ac-pulvinar-turpis-scelerisque/",
            "/ipsummerschool2022/2013/12/29/purus-rhoncus-et-lundium/",
            "/ipsummerschool2022/2013/12/29/et-auctor-tortor-nunc/",
            "/ipsummerschool2022/2013/12/29/porta-est-nascetur-proin/",
            "/ipsummerschool2022/2014/01/21/porta-est-nascetur-proin-3/",
            "/ipsummerschool2022/2014/01/21/purus-rhoncus-et-lundium-3/",
            "/ipsummerschool2022/2014/01/21/ac-pulvinar-turpis-scelerisque-2-2/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="number"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://www.anmil.it": {
        "urls": [
            "/webradio-anmil/buongiorno-dallanmil-del-23-febbraio/",
            "/regioni/anmil-marche-e-inail-firmano-protocollo-per-la-tutela-delle-persone-con-disabilita-da-lavoro/",
            "/regioni/resoconto-giornata-del-18-maggio-per-la-31a-giornata-regionale-promossa-da-anmil-lombardia/",
            "/regioni/anmil-napoli-allevento-in-corsa-per-il-lavoro-a-san-giorgio-a-cremano-per-la-ripartenza-del-lavoro-nel-sud/",
            "/regioni/regolamento-inail-per-interventi-a-favore-delle-persone-con-disabilita-da-lavoro/",
            "/regioni/anmil-ravenna-alla-cerimonia-in-memoria-delle-vittime-dellincidente-agip-organizzata-dalleni/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://blog.ufes.br": {
        "urls": [
            "/iurygoncalves/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://blogs.helsinki.fi": {
        "urls": [
            "/sosiologia-varjo-opas/129-2/",
            "/sosiologia-varjo-opas/152-2/",
            "/sosiologia-varjo-opas/140-2/",
            "/sosiologia-varjo-opas/231-2/",
            "/sosiologia-varjo-opas/136-2/",
            "/sosiologia-varjo-opas/6321-2/",
            "/sosiologia-varjo-opas/harj/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').click()""",
            """a3 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """x2 = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]').click()""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').click()""",
            """a5 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').click()""",
            """a7 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').click()""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://lis.uin-malang.ac.id": {
        "urls": [
            "/efektivitas-promosi-pada-perpustakaan-universitas-merdeka-malang-dengan-menggunakan-model-aida-attention-interest-desire-action-rosa-intania-hariyanto-putri-19680070/",
            "/pembuatan-website-sebagai-media-arsip-dan-informasi-izzulhaq-sain-fikri_19680058/",
            "/pengolahan-buku-hibah-pada-dinas-perpustakaan-dan-kearsipan-provinsi-kalimantan-barat-annisa-aklysta-leonisti-19680014-2/",
            "/penerapan-digitalisasi-koleksi-tugas-akhir/",
            "/pengelolaan-bahan-pustaka-di-dinas-perpustakaan-dan-kearsipan-kota-cilegon-laeli-nurhaliza_19680009/",
            "/sistem-temu-kembali-informasi-pengelolaan-arsip-status-di-dinas-perpustakaan-dan-kearsipan-kota-yogyakarta/",
            "/pemanfaatan-cloudinary-sebagai-alternatif-penyimpanan-arsip-digital-di-dinas-perpustakaan-dan-kearsipan-kota-yogyakarta-yuta-nika-19680024/",
            "/kegiatan-preservasi-dan-sosialisasi-pengelolaan-arsip-di-dinas-perpustakaan-umum-dan-arsip-daerah-kota-malang-luthfi-amangku-sasangko-19680030/",
            "/edukasi-pentingnya-pengelolaan-arsip-keluarga-bagi-anak-usia-sekolah-fauziatul-salsabila-19680018/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a9 = driver.find_element(By.XPATH, '//*[@id="wp-comment-cookies-consent"]').click()""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://www.intecap.edu.gt": {
        "urls": [
            "/centros/centroquetzaltenango/logo-intecap/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="send_comment"]').click()"""
        ]
    },
    "https://www.arpt.gov.gn": {
        "urls": [
            "/decision-fixant-les-conditions-dagrements-terminauxdes-installations-radioelectriques-et-des-installateurs-de-ces-equipements/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://ctlsites.uga.edu": {
        "urls": [
            "/apeclatbegin/the-dark-side-of-brasil-interview-with-nixiwaka-yawanawa/",
            "/apeclatbegin/we-would-rather-die-than-be-evicted/",
            "/apeclatbegin/62-2/",
            "/apeclatbegin/guarani-attacked-by-gunmen-in-brasil/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://www.vivianefreitas.com": {
        "urls": [
            "/ru/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/",
            "/ru/2020/06/05/3-%d1%87%d1%82%d0%be-%d1%8f-%d0%bc%d0%be%d0%b3%d1%83-%d0%be%d1%82%d0%b4%d0%b0%d1%82%d1%8c/",
            "/ru/2020/06/03/2-%d1%87%d1%82%d0%be-%d1%8f-%d0%bc%d0%be%d0%b3%d1%83-%d0%be%d1%82%d0%b4%d0%b0%d1%82%d1%8c/"
        ],
        "selenium_actions": [
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://mrl.upi.edu": {
        "urls": [
            "/beranda/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://idi.atu.edu.iq": {
        "urls": [
            "/?p=16355",
            "/?p=16364",
            "/?p=16357"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    "https://www.tribaltattootatuaggiroma.it": {
        "urls": [
            "/piercing-a-roma-lombelico/"
        ],
        "selenium_actions": [
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="commentform"]/div[4]/button').click()"""
        ]
    },
    "https://news.euspert.com": {
        "urls": [
            "/working-as-croupier-in-europe/",
            "/how-to-improve-your-concentration-and-stay-fully-focused/",
            "/how-to-improve-english-language-if-is-not-native-tongue/",
            "/where-its-possible-to-study-dentistry-in-central-europe/",
            "/bug-hunter-the-key-profession-in-cybersecurity-field-exclusive-interview-with-cybersecurity-expert-touseef-gul/",
            "/websummit-2019-international-institutions-and-government-organizations-hand-in-hand-with-innovative-startups/"
        ],
        "selenium_actions": [
            """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(comment)""",
            """a4 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(name)""",
            """a6 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)""",
            """a8 = driver.find_element(By.XPATH, '//*[@id="url"]').send_keys(www)""",
            """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""
        ]
    },
    # "https://main.ayush.gov.in/": {
    #     "urls": [
    #         "/common-monsoon-ailments-symptoms-prevention-and-treatment/",
    #         "/homoeopathy-as-a-career-2/",
    #         "/a-career-in-naturopathy/",
    #         "/a-career-in-unani-medicine/",
    #         "/ayurveda-as-a-career/",
    #         "/random-thoughts-on-the-4th-national-ayurveda-day-part-2/",
    #         "/traditional-food-recipes-from-ayush-systems/"
    #     ],
    #     "selenium_actions": [

    #     ]
    # },
}