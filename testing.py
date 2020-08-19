# you need to fix the SSL issue,
# found that the page is run by react, react scambles the code everytime, however,
# there is something interesting, always in the source of the page, there is a json object that has all the items
# it is a script tag at the end of the page that has attribute called data-js-react-on-rails-store
# it makes it too much easier to scroll through. see below.

import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--ignore-certificate-errors")
browser = webdriver.Chrome(options=options)

#initial request, then we make the code scroll through all the pages, it gets the total number of pages from the website, not manual.
browser.get('https://www.vinted.es/vetements?catalog[]=1&page=1/')
elem = browser.find_element_by_xpath('//*[@data-js-react-on-rails-store]').get_attribute('textContent')  # Find the search box
json_response = json.loads(elem)

firstpage = 1
lastpage = json_response["items"]["catalogItems"]["totalPages"]
itemCounter = 1

# start the things
for page_counter in range(firstpage, lastpage):
    #make the requets everytime
    url = 'https://www.vinted.es/vetements?catalog[]=1&page=' + str(page_counter)
    browser.get(url)
    elem = browser.find_element_by_xpath('//*[@data-js-react-on-rails-store]').get_attribute('textContent')  # Find the search box
    json_response = json.loads(elem)

    # loop through the items
    for key, value in json_response["items"]["byId"].items():
        print(itemCounter, ": Price is: ",value["price"], ", Username is:", value["user"]["login"],", Color is: ", value["color1_id"],", Favorites are: ",value["favourite_count"])
        itemCounter = itemCounter + 1
        # do whatever you want with the code here
    # remove this line, i just added so i don't print everything
    if page_counter == 2:
        exit()
exit()


# for your reference only

"""
    typical item by id is like This
    item:
        ID:
            "id":573167837,
            "title":"Sandalias de verano color mostaza",
            "brand_id":793983,
            "size_id":58,
            "status_id":6,
            "disposal_conditions":4,
            "user_id":39462440,
            "owner_id":null,
            "country_id":7,
            "catalog_id":207,
            "color1_id":29,
            "color2_id":null,
            "package_size_id":2,
            "is_hidden":0,
            "is_reserved":0,
            "reserved_for_user_id":null,
            "is_visible":1,
            "is_unisex":0,
            "is_closed":0,
            "is_admin_alerted":false,
            "active_bid_count":0,
            "favourite_count":2,
            "view_count":71,
            "moderation_status":0,
            "last_push_up_at":"2020-08-19T14:11:30+02:00",
            "description":"Sin uso\nPrecio de compra: 35\u20ac",
            "package_size_standard":true,
            "item_closing_action":null,
            "related_catalog_ids":[

            ],
            "related_catalogs_enabled":false,
            "size":"38",
            "brand":"Desconocida",
            "composition":"",
            "extra_conditions":"",
            "is_for_sell":true,
            "is_for_swap":false,
            "is_for_give_away":false,
            "is_handicraft":false,
            "is_draft":false,
            "label":"Desconocida",
            "real_value_numeric":null,
            "original_price_numeric":"25.0",
            "price_numeric":"25.0",
            "currency":"\u20ac",
            "created_at_ts":"2020-08-14T00:20:30+02:00",
            "updated_at_ts":"2020-08-19T14:11:30+02:00",
            "user_updated_at_ts":"2020-08-19T14:11:30+02:00",
            "photos":[
               {
                  "id":1994297432,
                  "image_no":1,
                  "width":800,
                  "height":360,
                  "dominant_color":"#5C3737",
                  "dominant_color_opaque":"#CEC3C3",
                  "url":"https://images.vinted.net/thumbs/f800/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-097d1c2749722250bf89d13a606e19c67f26dc3f",
                  "is_main":true,
                  "thumbnails":[
                     {
                        "type":"thumb70x100",
                        "url":"https://images.vinted.net/thumbs/70x100/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-19f49d8f1b10009fe75a0d28bcea69fddbca3393",
                        "width":70,
                        "height":100,
                        "original_size":null
                     },
                     {
                        "type":"thumb150x210",
                        "url":"https://images.vinted.net/thumbs/150x210/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-c60973db99b4ed86f58ccef4120bac6675c44b65",
                        "width":150,
                        "height":210,
                        "original_size":null
                     },
                     {
                        "type":"thumb310x430",
                        "url":"https://images.vinted.net/thumbs/310x430/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-ee62f88d64ae4821b706a2235d931871c66260ca",
                        "width":310,
                        "height":430,
                        "original_size":null
                     },
                     {
                        "type":"thumb428x624",
                        "url":"https://images.vinted.net/thumbs/f800/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-097d1c2749722250bf89d13a606e19c67f26dc3f",
                        "width":428,
                        "height":192,
                        "original_size":true
                     },
                     {
                        "type":"thumb624x428",
                        "url":"https://images.vinted.net/thumbs/f800/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-097d1c2749722250bf89d13a606e19c67f26dc3f",
                        "width":624,
                        "height":281,
                        "original_size":true
                     },
                     {
                        "type":"thumb364x428",
                        "url":"https://images.vinted.net/thumbs/f800/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-097d1c2749722250bf89d13a606e19c67f26dc3f",
                        "width":364,
                        "height":164,
                        "original_size":true
                     }
                  ],
                  "high_resolution":{
                     "id":"01_01596_TYd3RheN8XdPGP9m6SsVd4Es",
                     "timestamp":1597357231,
                     "orientation":null
                  },
                  "is_suspicious":false,
                  "full_size_url":"https://images.vinted.net/thumbs/01_01596_TYd3RheN8XdPGP9m6SsVd4Es.jpeg?1597357231-77d6d0b0dd1262a1589a6eb3ae5d3ab4cd720837"
               }
            ],
            "push_up_interval":604800,
            "can_be_sold":true,
            "can_feedback":false,
            "path":"/femmes/sandales/573167837-sandalias-de-verano-color-mostaza",
            "possible_to_request_reservation":true,
            "item_reservation_id":null,
            "receiver_id":null,
            "promoted_until":"2020-08-26T14:11:30+02:00",
            "discount_price_numeric":null,
            "badge":null,
            "reservation_requests_from_users":[

            ],
            "material_id":null,
            "author":null,
            "book_title":null,
            "isbn":null,
            "defect_ids":[

            ],
            "user":{
               "id":39462440,
               "anon_id":"216e8c63-3728-4a12-b093-e1bd3825b158",
               "login":"anaespinosa99",
               "real_name":null,
               "email":null,
               "birthday":null,
               "gender":"",
               "item_count":1,
               "msg_template_count":0,
               "given_item_count":0,
               "taken_item_count":0,
               "favourite_topic_count":0,
               "forum_msg_count":0,
               "forum_topic_count":0,
               "followers_count":0,
               "following_count":0,
               "following_brands_count":0,
               "positive_feedback_count":0,
               "neutral_feedback_count":0,
               "negative_feedback_count":0,
               "meeting_transaction_count":0,
               "account_status":9,
               "email_bounces":null,
               "feedback_reputation":0.0,
               "account_ban_date":null,
               "forum_ban_date":null,
               "is_on_holiday":false,
               "is_publish_photos_agreed":false,
               "is_shadow_banned":false,
               "is_identity":false,
               "allow_personalization":true,
               "expose_location":true,
               "third_party_tracking":true,
               "created_at":"2020-08-14T00:17:53+02:00",
               "last_loged_on_ts":"2020-08-19T14:10:37+02:00",
               "city_id":null,
               "city":"",
               "country_id":7,
               "country_code":"ES",
               "country_title_local":"España",
               "country_title":"España",
               "contacts_permission":null,
               "contacts":null,
               "photo":{
                  "id":33579940,
                  "width":800,
                  "height":800,
                  "temp_uuid":null,
                  "url":"https://images.vinted.net/thumbs/f800/01_0186b_vtq6VSFoSPeVp6pfFne1tXtR.jpeg?1597357074-e43ed80b60fcfafe1ee42017684606ec744db40b",
                  "dominant_color":"#31abc2",
                  "dominant_color_opaque":"#C1E6ED",
                  "thumbnails":[
                     {
                        "type":"thumb310",
                        "url":"https://images.vinted.net/thumbs/310x310/01_0186b_vtq6VSFoSPeVp6pfFne1tXtR.jpeg?1597357074-86678df2fc0c8fbebf418b4d9a0bb0437ea9d336",
                        "width":310,
                        "height":310,
                        "original_size":null
                     },
                     {
                        "type":"thumb150",
                        "url":"https://images.vinted.net/thumbs/150x150/01_0186b_vtq6VSFoSPeVp6pfFne1tXtR.jpeg?1597357074-8dbe65640ebb739a1f620f4e2eafa423427e068d",
                        "width":150,
                        "height":150,
                        "original_size":null
                     },
                     {
                        "type":"thumb100",
                        "url":"https://images.vinted.net/thumbs/100x100/01_0186b_vtq6VSFoSPeVp6pfFne1tXtR.jpeg?1597357074-04397352f61c8d18bcb6aa3a8615edc9efb09bea",
                        "width":100,
                        "height":100,
                        "original_size":null
                     },
                     {
                        "type":"thumb50",
                        "url":"https://images.vinted.net/thumbs/50x50/01_0186b_vtq6VSFoSPeVp6pfFne1tXtR.jpeg?1597357074-6e073a5f39bf4e2f6e02a342f9b69d047e997012",
                        "width":50,
                        "height":50,
                        "original_size":null
                     },
                     {
                        "type":"thumb20",
                        "url":"https://images.vinted.net/thumbs/20x20/01_0186b_vtq6VSFoSPeVp6pfFne1tXtR.jpeg?1597357074-31a591cdfcd8f8c1d752155cc493cac93be66441",
                        "width":20,
                        "height":20,
                        "original_size":null
                     }
                  ],
                  "is_suspicious":false,
                  "orientation":null,
                  "high_resolution":{
                     "id":"01_0186b_vtq6VSFoSPeVp6pfFne1tXtR",
                     "timestamp":1597357074,
                     "orientation":null
                  },
                  "full_size_url":"https://images.vinted.net/thumbs/01_0186b_vtq6VSFoSPeVp6pfFne1tXtR.jpeg?1597357074-e8700b07331b6afeb3e8635d753c0ec265fbd2f7"
               },
               "path":"/member/39462440-anaespinosa99",
               "is_god":false,
               "is_tester":false,
               "moderator":false,
               "volunteer_moderator":false,
               "hide_feedback":false,
               "can_post_big_forum_photos":false,
               "allow_direct_messaging":true,
               "bundle_discount":{
                  "id":6779792,
                  "user_id":39462440,
                  "enabled":false,
                  "minimal_item_count":2,
                  "fraction":"0.25",
                  "discounts":[
                     {
                        "minimal_item_count":2,
                        "fraction":"0.25"
                     },
                     {
                        "minimal_item_count":3,
                        "fraction":"0.3"
                     },
                     {
                        "minimal_item_count":5,
                        "fraction":"0.5"
                     }
                  ]
               },
               "donation_configuration":null,
               "total_items_count":1,
               "about":"",
               "vinted_club":{
                  "level":0,
                  "invited":false,
                  "active":false,
                  "landing_page_url":"https://www.vinted.fr/member/instructions/mobile/vinted_club"
               },
               "verification":{
                  "email":{
                     "valid":false,
                     "available":true
                  },
                  "facebook":{
                     "valid":true,
                     "verified_at":"2020-08-14T00:16:49+02:00",
                     "available":true,
                     "friend_count":null
                  },
                  "google":{
                     "valid":false,
                     "verified_at":null,
                     "available":true
                  },
                  "phone":{
                     "valid":false,
                     "verified_at":null,
                     "available":true
                  }
               },
               "closet_promoted_until":null,
               "avg_response_time":null,
               "carrier_ids":[
                  11,
                  33,
                  34,
                  36,
                  44,
                  4,
                  9
               ],
               "carriers_without_custom_ids":[
                  11,
                  33,
                  34,
                  36,
                  44,
                  4
               ],
               "updated_on":1597745855,
               "is_hated":false,
               "hates_you":false,
               "is_favourite":false,
               "profile_url":"https://www.vinted.es/member/39462440-anaespinosa99",
               "facebook_user_id":null,
               "is_online":false,
               "has_promoted_closet":false,
               "can_view_profile":true,
               "can_bundle":true,
               "last_loged_on":"hoy 02:10 PM",
               "accepted_pay_in_methods":[
                  {
                     "id":1,
                     "code":"CREDIT_CARD",
                     "requires_credit_card":true,
                     "event_tracking_code":"cc",
                     "icon":"credit-card",
                     "enabled":true,
                     "translated_name":"Tarjeta",
                     "note":"La información de tu tarjeta nunca será compartida con el vendedor. Vinted no almacena los datos de la tarjeta sin tu permiso."
                  },
                  {
                     "id":16,
                     "code":"APPLE_PAY",
                     "requires_credit_card":false,
                     "event_tracking_code":"apple_pay",
                     "icon":"apple-pay",
                     "enabled":true,
                     "translated_name":"Apple Pay",
                     "note":""
                  },
                  {
                     "id":10,
                     "code":"MANGOPAY_PAYPAL",
                     "requires_credit_card":false,
                     "event_tracking_code":"mangopay_paypal",
                     "icon":"paypal",
                     "enabled":true,
                     "translated_name":"PayPal",
                     "note":""
                  },
                  {
                     "id":9,
                     "code":"IDEAL",
                     "requires_credit_card":false,
                     "event_tracking_code":"ideal",
                     "icon":"ideal",
                     "enabled":true,
                     "translated_name":"iDeal",
                     "note":""
                  }
               ],
               "localization":"manual",
               "default_address":null
            },
            "can_edit":false,
            "can_delete":false,
            "can_request_reservation":false,
            "can_cancel_reservation_request":false,
            "can_reserve":false,
            "can_transfer":false,
            "instant_buy":true,
            "can_close":false,
            "can_buy":true,
            "can_bundle":true,
            "can_ask_seller":true,
            "can_favourite":false,
            "user_login":"anaespinosa99",
            "city_id":null,
            "city":"",
            "country":"España",
            "nearby":null,
            "distance":null,
            "promoted":true,
            "is_favourite":false,
            "is_mobile":false,
            "bump_badge_visible":false,
            "brand_dto":{
               "id":793983,
               "title":"Desconocida",
               "slug":"desconocida",
               "favourite_count":8782,
               "pretty_favourite_count":"8.8K",
               "item_count":210921,
               "pretty_item_count":"210.9K",
               "is_visible_in_listings":false,
               "path":"/brand/desconocida",
               "requires_authenticity_check":false,
               "url":"https://www.vinted.es/brand/desconocida",
               "is_favourite":false,
               "is_hated":false
            },
            "url":"https://www.vinted.es/femmes/sandales/573167837-sandalias-de-verano-color-mostaza",
            "accepted_pay_in_methods":[
               {
                  "id":1,
                  "code":"CREDIT_CARD",
                  "requires_credit_card":true,
                  "event_tracking_code":"cc",
                  "icon":"credit-card",
                  "enabled":true,
                  "translated_name":"Tarjeta",
                  "note":"La información de tu tarjeta nunca será compartida con el vendedor. Vinted no almacena los datos de la tarjeta sin tu permiso."
               },
               {
                  "id":10,
                  "code":"MANGOPAY_PAYPAL",
                  "requires_credit_card":false,
                  "event_tracking_code":"mangopay_paypal",
                  "icon":"paypal",
                  "enabled":true,
                  "translated_name":"PayPal",
                  "note":""
               }
            ],
            "created_at":"08/14 12:20 AM",
            "color1":"Mostaza",
            "color2":null,
            "material":null,
            "status":"Nuevo con etiquetas",
            "secure_purchase":true,
            "secure_purchase_badge":false,
            "performance":null,
            "stats_visible":true,
            "can_push_up":false,
            "price":"25,00 \u20ac",
            "discount_price":"",
            "real_value":"",
            "fees":null,
            "size_guide_faq_entry_id":510,
            "localization":"manual"

"""
