# # # import random
# # # import requests
# # # from bs4 import BeautifulSoup
# # # from django.shortcuts import render
# # # from requests.compat import quote_plus
# # # from selenium import webdriver
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.webdriver.support.ui import Select
# # # from . import models
# # #
# # # # Create your views here.
# # # driver = webdriver.Chrome(executable_path=r'C:/Users/acer/Downloads/chromedriver_win32/chromedriver.exe')
# # # # BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
# # # BASE_CRAIGSLIST_URL = 'https://www.yellowproxy.net/browse.php?u=https%3A%2F%2Flosangeles.craigslist.org%2Fd%2Ffor-sale%2Fsearch%2Fhhh%3Fquery%3D{}%26sort%3Drel&b=4&f=norefer'
# # # BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
# # # BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
# # #
# # #
# # #
# # # def home(request):
# # #     return render(request, "base.html")
# # #
# # #
# # # def new_search(request):
# # #     global proxies
# # #     search = request.POST.get('search')
# # #     models.Search.objects.create(search=search)
# # #     final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
# # #     driver.get(CROXYPROXY_SITE_URL)
# # #     search_box_input = driver.find_element_by_id("url")
# # #     search_box_input.send_keys(final_url)
# # #     search_box_input.submit()
# # #
# # #     soup = BeautifulSoup(driver.page_source, features="html.parser")
# # #     post_listings = soup.find_all('li', {'class': 'result-row'})
# # #
# # #     final_postings = []
# # #     for post in post_listings:
# # #         post_title = post.find(class_='result-title').text
# # #         post_url = post.find('a').get('href')
# # #         if post.find(class_='result-price'):
# # #             post_price = post.find(class_='result-price').text
# # #         else:
# # #             post_price = 'N/A'
# # #
# # #         if post.find(class_='result-image').get('data-ids'):
# # #             post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
# # #             post_image_url = BASE_IMAGE_URL.format(post_image_id)
# # #         else:
# # #             post_image_url = 'https://craigslist.org/images/peace.jpg'
# # #
# # #         final_postings.append((post_title, post_url, post_price, post_image_url))
# # #     # driver.close()
# # #     stuff_for_frontend = {
# # #         'search': search, 'final_postings': final_postings
# # #     }
# # #     return render(request, 'my_app/new_search.html', stuff_for_frontend)
# #
# # # if 'https://losangeles.craigslist.org/sfv/spo/d/glendale-stiga-ping-pong-table-tennis/7269049111.html' == 'https://losangeles.craigslist.org/sfv/spo/d/glendale-stiga-ping-pong-table-tennis/7269049111.html/':
# # #     print('same')
# # # else:
# # #     print('different')
# #
# #
# # links = [['home', 'contact', 'exit'], ['play', 'points', 'transfers'], ['status', 'gameweek kings'], 'editor picks',
# #          'blogs']
# # h4 = [['alabama', 'losangeles', 'carlifonia', 'alaska', 'michigan', 'waschigton dc', 'texas', 'las vegas', 'downtown'],
# #       ['fdsaklf', 'kdk;dfa', 'dkjahfd']]
# # h1 = ['us', 'uk', 'spain', 'germany', 'netherlands', 'china', 'america', 'europe']
# #
# # temp_header = h1[0]
# # h1[0] = dict(header=(h4[0], links[0]))
# # md = h1[0]
# # md[temp_header] = md.pop('header')
# # # print(md)
# #
# #
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome(executable_path=r'C:/Users/acer/Downloads/chromedriver_win32/chromedriver.exe')
# driver.get('https://hide.me/en/proxy')
# proxy_options_dropdown = driver.find_elements_by_class_name('proxy_option')
# proxy_options_dropdown[1].click()
# encrypt_url_checkbox = driver.find_element_by_name("encodeURL")
# encrypt_url_checkbox.click()
# search_box_input = driver.find_element_by_id("u")
# search_box_input.send_keys('https://www.craigslist.org/about/sites')
# search_box_input.submit()
#
# soup = BeautifulSoup(driver.page_source, features='html.parser')
# links = soup.find_all('a')
# links = links[16:]
# # for link in links:
# #     raw_link = link.get('href')
# #     print(raw_link)
# #     print('TYPE: ', type(raw_link))
#
# # count = 0
# links_list = []
# for link in links:
#     raw_link = link.get('href')
#     if raw_link is None:
#         continue
#     split_raw_link = raw_link.split('/go.php?u=https%3A%2F%2F')
#     split_raw_link = ''.join(split_raw_link)
#     split_raw_link = split_raw_link.split('%2F&b=4')
#     processed_link = split_raw_link[0]
#     print(list(processed_link))
#     links_list.append(processed_link)
#     # count += 1
#     if processed_link == 'tunis.craigslist.org':
#         break
# # print('COUNT: ',count)
#
# uls = soup.find_all('ul')
# uls = uls[1:]
# # count2 = 0
# lt_list = []
# for ul in uls:
#     link_text = ul.text
#     link_text = link_text.strip()
#     # ul_list = list(link_text)
#     # print('*****')
#     # print(ul_list)
#     # length = 0
#     # if '\n' in ul_list:
#     #     length = ul_list.count('\n')
#     # length += 1
#     # count2 += length
#     print(list(link_text))
#     lt_list.append(link_text)
#     if 'tunisia' in link_text:
#         break
#
# print(links_list)
# print(lt_list)
# # print('count2: ', count2)
#
#
# # # links = soup.find_all('li a')
# # # ml = []
# # #
# # # uls = soup.find_all('ul')
# # # print(uls)
# # # try:
# # #     print()
# # #     print()
# # #     # print('PRINTING ULS.TEXT')
# # #     # for ul in uls:
# # #     #     print(ul.text)
# # #     print('PRINTING UL.HREF')
# # #     print(uls.find('li'))
# # #     print('PRINTING UL.HREF 2')
# # #     for ul in uls:
# # #         print(ul.find('li'))
# # #
# # # except:
# # #     print('CANT PRINT ULS.TEXT')
# # #     try:
# # #         print()
# # #         print()
# # #         print('FINDING A TAGS')
# # #         for ul in uls:
# # #             li = ul.find('a').get('href')
# # #             ml.append(li)
# # #         print(ml)
# # #     except:
# # #         print('CANT FIND A TAGS')
# #
# # # for ul in uls:
# # #     links = ul.find_all('li')
# # #     # link_text = ul.find('a').text
# # #     ml.append((links))
# #
# # # for list_item in ml:
# # #     print(list_item)
# #
# # # headers = soup.find_all('h1')
# # # for header in headers:
# # #     print("'" + header.text + "'" + ',')
# #
# headers = ['US',
#            'Canada',
#            'Europe',
#            'Asia, Pacific and Middle East',
#            'Oceania',
#            'Latin America and Caribbean',
#            'Africa']
# sub_headers = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'TERRITORIES', 'ALBERTA', 'BRITISH COLUMBIA', 'MANITOBA', 'NEW BRUNSWICK', 'NEWFOUNDLAND AND LABRADOR', 'NORTHWEST TERRITORIES', 'NOVA SCOTIA', 'ONTARIO', 'PRINCE EDWARD ISLAND', 'QUEBEC', 'SASKATCHEWAN', 'YUKON TERRITORY', 'AUSTRIA', 'BELGIUM', 'BULGARIA', 'CROATIA', 'CZECH REPUBLIC', 'DENMARK', 'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HUNGARY', 'ICELAND', 'IRELAND', 'ITALY', 'LUXEMBOURG', 'NETHERLANDS', 'NORWAY', 'POLAND', 'PORTUGAL', 'ROMANIA', 'RUSSIAN FEDERATION', 'SPAIN', 'SWEDEN', 'SWITZERLAND', 'TURKEY', 'UKRAINE', 'UNITED KINGDOM', 'BANGLADESH', 'CHINA', 'GUAM / MICRONESIA', 'HONG KONG', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'ISRAEL AND PALESTINE', 'JAPAN', 'KOREA', 'KUWAIT', 'LEBANON', 'MALAYSIA', 'PAKISTAN', 'PHILIPPINES', 'SINGAPORE', 'TAIWAN', 'THAILAND', 'UNITED ARAB EMIRATES', 'VIETNAM', 'AUSTRALIA', 'NEW ZEALAND', 'ARGENTINA', 'BOLIVIA', 'BRAZIL', 'CARIBBEAN ISLANDS', 'CHILE', 'COLOMBIA', 'COSTA RICA', 'DOMINICAN REPUBLIC', 'ECUADOR', 'EL SALVADOR', 'GUATEMALA', 'MEXICO', 'NICARAGUA', 'PANAMA', 'PERU', 'PUERTO RICO', 'URUGUAY', 'VENEZUELA', 'VIRGIN ISLANDS, U.S.', 'EGYPT', 'ETHIOPIA', 'GHANA', 'KENYA', 'MOROCCO', 'SOUTH AFRICA', 'TUNISIA']
# sub_headers = ['Alabama',
#                'Alaska',
#                'Arizona',
#                'Arkansas',
#                'California',
#                'Colorado',
#                'Connecticut',
#                'Delaware',
#                'District of Columbia',
#                'Florida',
#                'Georgia',
#                'Hawaii',
#                'Idaho',
#                'Illinois',
#                'Indiana',
#                'Iowa',
#                'Kansas',
#                'Kentucky',
#                'Louisiana',
#                'Maine',
#                'Maryland',
#                'Massachusetts',
#                'Michigan',
#                'Minnesota',
#                'Mississippi',
#                'Missouri',
#                'Montana',
#                'Nebraska',
#                'Nevada',
#                'New Hampshire',
#                'New Jersey',
#                'New Mexico',
#                'New York',
#                'North Carolina',
#                'North Dakota',
#                'Ohio',
#                'Oklahoma',
#                'Oregon',
#                'Pennsylvania',
#                'Rhode Island',
#                'South Carolina',
#                'South Dakota',
#                'Tennessee',
#                'Texas',
#                'Utah',
#                'Vermont',
#                'Virginia',
#                'Washington',
#                'West Virginia',
#                'Wisconsin',
#                'Wyoming',
#                'Territories',
#                'Alberta',
#                'British Columbia',
#                'Manitoba',
#                'New Brunswick',
#                'Newfoundland and Labrador',
#                'Northwest Territories',
#                'Nova Scotia',
#                'Ontario',
#                'Prince Edward Island',
#                'Quebec',
#                'Saskatchewan',
#                'Yukon Territory',
#                'Austria',
#                'Belgium',
#                'Bulgaria',
#                'Croatia',
#                'Czech Republic',
#                'Denmark',
#                'Finland',
#                'France',
#                'Germany',
#                'Greece',
#                'Hungary',
#                'Iceland',
#                'Ireland',
#                'Italy',
#                'Luxembourg',
#                'Netherlands',
#                'Norway',
#                'Poland',
#                'Portugal',
#                'Romania',
#                'Russian Federation',
#                'Spain',
#                'Sweden',
#                'Switzerland',
#                'Turkey',
#                'Ukraine',
#                'United Kingdom',
#                'Bangladesh',
#                'China',
#                'Guam / Micronesia',
#                'Hong Kong',
#                'India',
#                'Indonesia',
#                'Iran',
#                'Iraq',
#                'Israel and Palestine',
#                'Japan',
#                'Korea',
#                'Kuwait',
#                'Lebanon',
#                'Malaysia',
#                'Pakistan',
#                'Philippines',
#                'Singapore',
#                'Taiwan',
#                'Thailand',
#                'United Arab Emirates',
#                'Vietnam',
#                'Australia',
#                'New Zealand',
#                'Argentina',
#                'Bolivia',
#                'Brazil',
#                'Caribbean Islands',
#                'Chile',
#                'Colombia',
#                'Costa Rica',
#                'Dominican Republic',
#                'Ecuador',
#                'El Salvador',
#                'Guatemala',
#                'Mexico',
#                'Nicaragua',
#                'Panama',
#                'Peru',
#                'Puerto Rico',
#                'Uruguay',
#                'Venezuela',
#                'Virgin Islands, U.S.',
#                'Egypt',
#                'Ethiopia',
#                'Ghana',
#                'Kenya',
#                'Morocco',
#                'South Africa',
#                'Tunisia']
# for sb in sub_headers:
#     sub_headers[sub_headers.index(sb)] = sb.upper()
#
# print(sub_headers)
# links = ['', '', 'auburn.craigslist.org', 'bham.craigslist.org', 'dothan.craigslist.org', 'shoals.craigslist.org', 'gadsden.craigslist.org', 'huntsville.craigslist.org', 'mobile.craigslist.org', 'montgomery.craigslist.org', 'tuscaloosa.craigslist.org', '', 'anchorage.craigslist.org', 'fairbanks.craigslist.org', 'kenai.craigslist.org', 'juneau.craigslist.org', '', 'flagstaff.craigslist.org', 'mohave.craigslist.org', 'phoenix.craigslist.org', 'prescott.craigslist.org', 'showlow.craigslist.org', 'sierravista.craigslist.org', 'tucson.craigslist.org', 'yuma.craigslist.org', '', 'fayar.craigslist.org', 'fortsmith.craigslist.org', 'jonesboro.craigslist.org', 'littlerock.craigslist.org', 'texarkana.craigslist.org', '', 'bakersfield.craigslist.org', 'chico.craigslist.org', 'fresno.craigslist.org', 'goldcountry.craigslist.org', 'hanford.craigslist.org', 'humboldt.craigslist.org', 'imperial.craigslist.org', 'inlandempire.craigslist.org', 'losangeles.craigslist.org', 'mendocino.craigslist.org', 'merced.craigslist.org', 'modesto.craigslist.org', 'monterey.craigslist.org', 'orangecounty.craigslist.org', 'palmsprings.craigslist.org', 'redding.craigslist.org', 'sacramento.craigslist.org', 'sandiego.craigslist.org', 'sfbay.craigslist.org', 'slo.craigslist.org', 'santabarbara.craigslist.org', 'santamaria.craigslist.org', 'siskiyou.craigslist.org', 'stockton.craigslist.org', 'susanville.craigslist.org', 'ventura.craigslist.org', 'visalia.craigslist.org', 'yubasutter.craigslist.org', '', 'boulder.craigslist.org', 'cosprings.craigslist.org', 'denver.craigslist.org', 'eastco.craigslist.org', 'fortcollins.craigslist.org', 'rockies.craigslist.org', 'pueblo.craigslist.org', 'westslope.craigslist.org', '', 'newlondon.craigslist.org', 'hartford.craigslist.org', 'newhaven.craigslist.org', 'nwct.craigslist.org', '', 'delaware.craigslist.org', '', 'washingtondc.craigslist.org', '', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fbrw', 'daytona.craigslist.org', 'keys.craigslist.org', 'fortlauderdale.craigslist.org', 'fortmyers.craigslist.org', 'gainesville.craigslist.org', 'cfl.craigslist.org', 'jacksonville.craigslist.org', 'lakeland.craigslist.org', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc', 'lakecity.craigslist.org', 'ocala.craigslist.org', 'okaloosa.craigslist.org', 'orlando.craigslist.org', 'panamacity.craigslist.org', 'pensacola.craigslist.org', 'sarasota.craigslist.org', 'miami.craigslist.org', 'spacecoast.craigslist.org', 'staugustine.craigslist.org', 'tallahassee.craigslist.org', 'tampa.craigslist.org', 'treasure.craigslist.org', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc', '', 'albanyga.craigslist.org', 'athensga.craigslist.org', 'atlanta.craigslist.org', 'augusta.craigslist.org', 'brunswick.craigslist.org', 'columbusga.craigslist.org', 'macon.craigslist.org', 'nwga.craigslist.org', 'savannah.craigslist.org', 'statesboro.craigslist.org', 'valdosta.craigslist.org', '', 'honolulu.craigslist.org', '', 'boise.craigslist.org', 'eastidaho.craigslist.org', 'lewiston.craigslist.org', 'twinfalls.craigslist.org', '', 'bn.craigslist.org', 'chambana.craigslist.org', 'chicago.craigslist.org', 'decatur.craigslist.org', 'lasalle.craigslist.org', 'mattoon.craigslist.org', 'peoria.craigslist.org', 'rockford.craigslist.org', 'carbondale.craigslist.org', 'springfieldil.craigslist.org', 'quincy.craigslist.org', '', 'bloomington.craigslist.org', 'evansville.craigslist.org', 'fortwayne.craigslist.org', 'indianapolis.craigslist.org', 'kokomo.craigslist.org', 'tippecanoe.craigslist.org', 'muncie.craigslist.org', 'richmondin.craigslist.org', 'southbend.craigslist.org', 'terrehaute.craigslist.org', '', 'ames.craigslist.org', 'cedarrapids.craigslist.org', 'desmoines.craigslist.org', 'dubuque.craigslist.org', 'fortdodge.craigslist.org', 'iowacity.craigslist.org', 'masoncity.craigslist.org', 'quadcities.craigslist.org', 'siouxcity.craigslist.org', 'ottumwa.craigslist.org', 'waterloo.craigslist.org', '', 'lawrence.craigslist.org', 'ksu.craigslist.org', 'nwks.craigslist.org', 'salina.craigslist.org', 'seks.craigslist.org', 'swks.craigslist.org', 'topeka.craigslist.org', 'wichita.craigslist.org', '', 'bgky.craigslist.org', 'eastky.craigslist.org', 'lexington.craigslist.org', 'louisville.craigslist.org', 'owensboro.craigslist.org', 'westky.craigslist.org', '', 'batonrouge.craigslist.org', 'cenla.craigslist.org', 'houma.craigslist.org', 'lafayette.craigslist.org', 'lakecharles.craigslist.org', 'monroe.craigslist.org', 'neworleans.craigslist.org', 'shreveport.craigslist.org', '', 'maine.craigslist.org', '', 'annapolis.craigslist.org', 'baltimore.craigslist.org', 'easternshore.craigslist.org', 'frederick.craigslist.org', 'smd.craigslist.org', 'westmd.craigslist.org', '', 'boston.craigslist.org', 'capecod.craigslist.org', 'southcoast.craigslist.org', 'westernmass.craigslist.org', 'worcester.craigslist.org', '', 'annarbor.craigslist.org', 'battlecreek.craigslist.org', 'centralmich.craigslist.org', 'detroit.craigslist.org', 'flint.craigslist.org', 'grandrapids.craigslist.org', 'holland.craigslist.org', 'jxn.craigslist.org', 'kalamazoo.craigslist.org', 'lansing.craigslist.org', 'monroemi.craigslist.org', 'muskegon.craigslist.org', 'nmi.craigslist.org', 'porthuron.craigslist.org', 'saginaw.craigslist.org', 'swmi.craigslist.org', 'thumb.craigslist.org', 'up.craigslist.org', '', 'bemidji.craigslist.org', 'brainerd.craigslist.org', 'duluth.craigslist.org', 'mankato.craigslist.org', 'minneapolis.craigslist.org', 'rmn.craigslist.org', 'marshall.craigslist.org', 'stcloud.craigslist.org', '', 'gulfport.craigslist.org', 'hattiesburg.craigslist.org', 'jackson.craigslist.org', 'meridian.craigslist.org', 'northmiss.craigslist.org', 'natchez.craigslist.org', '', 'columbiamo.craigslist.org', 'joplin.craigslist.org', 'kansascity.craigslist.org', 'kirksville.craigslist.org', 'loz.craigslist.org', 'semo.craigslist.org', 'springfield.craigslist.org', 'stjoseph.craigslist.org', 'stlouis.craigslist.org', '', 'billings.craigslist.org', 'bozeman.craigslist.org', 'butte.craigslist.org', 'greatfalls.craigslist.org', 'helena.craigslist.org', 'kalispell.craigslist.org', 'missoula.craigslist.org', 'montana.craigslist.org', '', 'grandisland.craigslist.org', 'lincoln.craigslist.org', 'northplatte.craigslist.org', 'omaha.craigslist.org', 'scottsbluff.craigslist.org', '', 'elko.craigslist.org', 'lasvegas.craigslist.org', 'reno.craigslist.org', '', 'nh.craigslist.org', '', 'cnj.craigslist.org', 'jerseyshore.craigslist.org', 'newjersey.craigslist.org', 'southjersey.craigslist.org', '', 'albuquerque.craigslist.org', 'clovis.craigslist.org', 'farmington.craigslist.org', 'lascruces.craigslist.org', 'roswell.craigslist.org', 'santafe.craigslist.org', '', 'albany.craigslist.org', 'binghamton.craigslist.org', 'buffalo.craigslist.org', 'catskills.craigslist.org', 'chautauqua.craigslist.org', 'elmira.craigslist.org', 'fingerlakes.craigslist.org', 'glensfalls.craigslist.org', 'hudsonvalley.craigslist.org', 'ithaca.craigslist.org', 'longisland.craigslist.org', 'newyork.craigslist.org', 'oneonta.craigslist.org', 'plattsburgh.craigslist.org', 'potsdam.craigslist.org', 'rochester.craigslist.org', 'syracuse.craigslist.org', 'twintiers.craigslist.org', 'utica.craigslist.org', 'watertown.craigslist.org', '', 'asheville.craigslist.org', 'boone.craigslist.org', 'charlotte.craigslist.org', 'eastnc.craigslist.org', 'fayetteville.craigslist.org', 'greensboro.craigslist.org', 'hickory.craigslist.org', 'onslow.craigslist.org', 'outerbanks.craigslist.org', 'raleigh.craigslist.org', 'wilmington.craigslist.org', 'winstonsalem.craigslist.org', '', 'bismarck.craigslist.org', 'fargo.craigslist.org', 'grandforks.craigslist.org', 'nd.craigslist.org', '', 'akroncanton.craigslist.org', 'ashtabula.craigslist.org', 'athensohio.craigslist.org', 'chillicothe.craigslist.org', 'cincinnati.craigslist.org', 'cleveland.craigslist.org', 'columbus.craigslist.org', 'dayton.craigslist.org', 'limaohio.craigslist.org', 'mansfield.craigslist.org', 'sandusky.craigslist.org', 'toledo.craigslist.org', 'tuscarawas.craigslist.org', 'youngstown.craigslist.org', 'zanesville.craigslist.org', '', 'lawton.craigslist.org', 'enid.craigslist.org', 'oklahomacity.craigslist.org', 'stillwater.craigslist.org', 'tulsa.craigslist.org', '', 'bend.craigslist.org', 'corvallis.craigslist.org', 'eastoregon.craigslist.org', 'eugene.craigslist.org', 'klamath.craigslist.org', 'medford.craigslist.org', 'oregoncoast.craigslist.org', 'portland.craigslist.org', 'roseburg.craigslist.org', 'salem.craigslist.org', '', 'altoona.craigslist.org', 'chambersburg.craigslist.org', 'erie.craigslist.org', 'harrisburg.craigslist.org', 'lancaster.craigslist.org', 'allentown.craigslist.org', 'meadville.craigslist.org', 'philadelphia.craigslist.org', 'pittsburgh.craigslist.org', 'poconos.craigslist.org', 'reading.craigslist.org', 'scranton.craigslist.org', 'pennstate.craigslist.org', 'williamsport.craigslist.org', 'york.craigslist.org', '', 'providence.craigslist.org', '', 'charleston.craigslist.org', 'columbia.craigslist.org', 'florencesc.craigslist.org', 'greenville.craigslist.org', 'hiltonhead.craigslist.org', 'myrtlebeach.craigslist.org', '', 'nesd.craigslist.org', 'csd.craigslist.org', 'rapidcity.craigslist.org', 'siouxfalls.craigslist.org', 'sd.craigslist.org', '', 'chattanooga.craigslist.org', 'clarksville.craigslist.org', 'cookeville.craigslist.org', 'jacksontn.craigslist.org', 'knoxville.craigslist.org', 'memphis.craigslist.org', 'nashville.craigslist.org', 'tricities.craigslist.org', '', 'abilene.craigslist.org', 'amarillo.craigslist.org', 'austin.craigslist.org', 'beaumont.craigslist.org', 'brownsville.craigslist.org', 'collegestation.craigslist.org', 'corpuschristi.craigslist.org', 'dallas.craigslist.org', 'nacogdoches.craigslist.org', 'delrio.craigslist.org', 'elpaso.craigslist.org', 'galveston.craigslist.org', 'houston.craigslist.org', 'killeen.craigslist.org', 'laredo.craigslist.org', 'lubbock.craigslist.org', 'mcallen.craigslist.org', 'odessa.craigslist.org', 'sanangelo.craigslist.org', 'sanantonio.craigslist.org', 'sanmarcos.craigslist.org', 'bigbend.craigslist.org', 'texoma.craigslist.org', 'easttexas.craigslist.org', 'victoriatx.craigslist.org', 'waco.craigslist.org', 'wichitafalls.craigslist.org', '', 'logan.craigslist.org', 'ogden.craigslist.org', 'provo.craigslist.org', 'saltlakecity.craigslist.org', 'stgeorge.craigslist.org', '', 'vermont.craigslist.org', '', 'charlottesville.craigslist.org', 'danville.craigslist.org', 'fredericksburg.craigslist.org', 'norfolk.craigslist.org', 'harrisonburg.craigslist.org', 'lynchburg.craigslist.org', 'blacksburg.craigslist.org', 'richmond.craigslist.org', 'roanoke.craigslist.org', 'swva.craigslist.org', 'winchester.craigslist.org', '', 'bellingham.craigslist.org', 'kpr.craigslist.org', 'moseslake.craigslist.org', 'olympic.craigslist.org', 'pullman.craigslist.org', 'seattle.craigslist.org', 'skagit.craigslist.org', 'spokane.craigslist.org', 'wenatchee.craigslist.org', 'yakima.craigslist.org', '', 'charlestonwv.craigslist.org', 'martinsburg.craigslist.org', 'huntington.craigslist.org', 'morgantown.craigslist.org', 'wheeling.craigslist.org', 'parkersburg.craigslist.org', 'swv.craigslist.org', 'wv.craigslist.org', '', 'appleton.craigslist.org', 'eauclaire.craigslist.org', 'greenbay.craigslist.org', 'janesville.craigslist.org', 'racine.craigslist.org', 'lacrosse.craigslist.org', 'madison.craigslist.org', 'milwaukee.craigslist.org', 'northernwi.craigslist.org', 'sheboygan.craigslist.org', 'wausau.craigslist.org', '', 'wyoming.craigslist.org', '', 'micronesia.craigslist.org', 'puertorico.craigslist.org', 'virgin.craigslist.org', 'calgary.craigslist.org', '', 'edmonton.craigslist.org', 'ftmcmurray.craigslist.org', 'lethbridge.craigslist.org', 'hat.craigslist.org', 'peace.craigslist.org', 'reddeer.craigslist.org', 'cariboo.craigslist.org', '', 'comoxvalley.craigslist.org', 'abbotsford.craigslist.org', 'kamloops.craigslist.org', 'kelowna.craigslist.org', 'kootenays.craigslist.org', 'nanaimo.craigslist.org', 'princegeorge.craigslist.org', 'skeena.craigslist.org', 'sunshine.craigslist.org', 'vancouver.craigslist.org', 'victoria.craigslist.org', 'whistler.craigslist.org', 'winnipeg.craigslist.org', '', 'newbrunswick.craigslist.org', '', 'newfoundland.craigslist.org', '', 'territories.craigslist.org', '', 'yellowknife.craigslist.org', 'halifax.craigslist.org', '', 'barrie.craigslist.org', '', 'belleville.craigslist.org', 'brantford.craigslist.org', 'chatham.craigslist.org', 'cornwall.craigslist.org', 'guelph.craigslist.org', 'hamilton.craigslist.org', 'kingston.craigslist.org', 'kitchener.craigslist.org', 'londonon.craigslist.org', 'niagara.craigslist.org', 'ottawa.craigslist.org', 'owensound.craigslist.org', 'peterborough.craigslist.org', 'sarnia.craigslist.org', 'soo.craigslist.org', 'sudbury.craigslist.org', 'thunderbay.craigslist.org', 'toronto.craigslist.org', 'windsor.craigslist.org', 'pei.craigslist.org', '', 'montreal.craigslist.org', '', 'quebec.craigslist.org', 'saguenay.craigslist.org', 'sherbrooke.craigslist.org', 'troisrivieres.craigslist.org', '', '', 'regina.craigslist.org', 'saskatoon.craigslist.org', '', 'whitehorse.craigslist.org', 'vienna.craigslist.at', '', 'brussels.craigslist.org', '', 'bulgaria.craigslist.org', '', 'zagreb.craigslist.org', '', 'prague.craigslist.cz', '', 'copenhagen.craigslist.org', '', 'helsinki.craigslist.fi', '', 'bordeaux.craigslist.org', '', 'rennes.craigslist.org', 'grenoble.craigslist.org', 'lille.craigslist.org', 'loire.craigslist.org', 'lyon.craigslist.org', 'marseilles.craigslist.org', 'montpellier.craigslist.org', 'cotedazur.craigslist.org', 'rouen.craigslist.org', 'paris.craigslist.org', 'strasbourg.craigslist.org', 'toulouse.craigslist.org', 'berlin.craigslist.de', '', 'bremen.craigslist.de', 'cologne.craigslist.de', 'dresden.craigslist.de', 'dusseldorf.craigslist.de', 'essen.craigslist.de', 'frankfurt.craigslist.de', 'hamburg.craigslist.de', 'hannover.craigslist.de', 'heidelberg.craigslist.de', 'kaiserslautern.craigslist.de', 'leipzig.craigslist.de', 'munich.craigslist.de', 'nuremberg.craigslist.de', 'stuttgart.craigslist.de', 'athens.craigslist.gr', '', 'budapest.craigslist.org', '', 'reykjavik.craigslist.org', '', 'dublin.craigslist.org', '', 'bologna.craigslist.it', '', 'florence.craigslist.it', 'genoa.craigslist.it', 'milan.craigslist.it', 'naples.craigslist.it', 'perugia.craigslist.it', 'rome.craigslist.it', 'sardinia.craigslist.it', 'sicily.craigslist.it', 'torino.craigslist.it', 'venice.craigslist.it', 'luxembourg.craigslist.org', '', 'amsterdam.craigslist.org', '', 'oslo.craigslist.org', '', 'warsaw.craigslist.pl', '', 'faro.craigslist.pt', '', 'lisbon.craigslist.pt', 'porto.craigslist.pt', 'bucharest.craigslist.org', '', 'moscow.craigslist.org', '', 'stpetersburg.craigslist.org', 'alicante.craigslist.es', '', 'baleares.craigslist.es', 'barcelona.craigslist.es', 'bilbao.craigslist.es', '', 'cadiz.craigslist.es', 'canarias.craigslist.es', 'granada.craigslist.es', 'madrid.craigslist.es', 'malaga.craigslist.es', 'sevilla.craigslist.es', 'valencia.craigslist.es', '', 'stockholm.craigslist.se', '', 'basel.craigslist.ch', 'bern.craigslist.ch', 'geneva.craigslist.ch', 'lausanne.craigslist.ch', 'zurich.craigslist.ch', '', 'istanbul.craigslist.com.tr', '', 'ukraine.craigslist.org', '', 'aberdeen.craigslist.co.uk', 'bath.craigslist.co.uk', 'belfast.craigslist.co.uk', 'birmingham.craigslist.co.uk', 'brighton.craigslist.co.uk', 'bristol.craigslist.co.uk', 'cambridge.craigslist.co.uk', 'cardiff.craigslist.co.uk', 'coventry.craigslist.co.uk', 'derby.craigslist.co.uk', 'devon.craigslist.co.uk', 'dundee.craigslist.co.uk', 'norwich.craigslist.co.uk', 'eastmids.craigslist.co.uk', 'edinburgh.craigslist.co.uk', 'essex.craigslist.co.uk', 'glasgow.craigslist.co.uk', 'hampshire.craigslist.co.uk', 'kent.craigslist.co.uk', 'leeds.craigslist.co.uk', 'liverpool.craigslist.co.uk', 'london.craigslist.co.uk', 'manchester.craigslist.co.uk', 'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk', 'oxford.craigslist.co.uk', 'sheffield.craigslist.co.uk', 'bangladesh.craigslist.org', '', 'beijing.craigslist.com.cn', '', 'chengdu.craigslist.com.cn', 'chongqing.craigslist.com.cn', 'dalian.craigslist.com.cn', 'guangzhou.craigslist.com.cn', 'hangzhou.craigslist.com.cn', 'nanjing.craigslist.com.cn', 'shanghai.craigslist.com.cn', 'shenyang.craigslist.com.cn', 'shenzhen.craigslist.com.cn', 'wuhan.craigslist.com.cn', 'xian.craigslist.com.cn', 'micronesia.craigslist.org', '', 'hongkong.craigslist.hk', '', 'ahmedabad.craigslist.co.in', '', 'bangalore.craigslist.co.in', 'bhubaneswar.craigslist.co.in', 'chandigarh.craigslist.co.in', 'chennai.craigslist.co.in', 'delhi.craigslist.co.in', 'goa.craigslist.co.in', 'hyderabad.craigslist.co.in', 'indore.craigslist.co.in', 'jaipur.craigslist.co.in', 'kerala.craigslist.co.in', 'kolkata.craigslist.co.in', 'lucknow.craigslist.co.in', 'mumbai.craigslist.co.in', 'pune.craigslist.co.in', 'surat.craigslist.co.in', 'jakarta.craigslist.org', '', 'tehran.craigslist.org', '', 'baghdad.craigslist.org', '', 'haifa.craigslist.org', '', 'jerusalem.craigslist.org', 'telaviv.craigslist.org', 'ramallah.craigslist.org', 'fukuoka.craigslist.jp', '', 'hiroshima.craigslist.jp', 'nagoya.craigslist.jp', 'okinawa.craigslist.jp', 'osaka.craigslist.jp', 'sapporo.craigslist.jp', 'sendai.craigslist.jp', 'tokyo.craigslist.jp', 'seoul.craigslist.co.kr', '', 'kuwait.craigslist.org', '', 'beirut.craigslist.org', '', 'malaysia.craigslist.org', '', 'pakistan.craigslist.org', '', 'bacolod.craigslist.com.ph', '', 'naga.craigslist.com.ph', 'cdo.craigslist.com.ph', 'cebu.craigslist.com.ph', 'davaocity.craigslist.com.ph', 'iloilo.craigslist.com.ph', 'manila.craigslist.com.ph', 'pampanga.craigslist.com.ph', 'zamboanga.craigslist.com.ph', 'singapore.craigslist.com.sg', '', 'taipei.craigslist.com.tw', '', 'bangkok.craigslist.co.th', '', 'dubai.craigslist.org', '', 'vietnam.craigslist.org', '', 'adelaide.craigslist.com.au', 'brisbane.craigslist.com.au', '', 'cairns.craigslist.com.au', 'canberra.craigslist.com.au', 'darwin.craigslist.com.au', 'goldcoast.craigslist.com.au', 'melbourne.craigslist.com.au', 'ntl.craigslist.com.au', 'perth.craigslist.com.au', 'sydney.craigslist.com.au', 'hobart.craigslist.com.au', 'wollongong.craigslist.com.au', 'auckland.craigslist.org', 'christchurch.craigslist.org', '', 'dunedin.craigslist.co.nz', 'wellington.craigslist.org', 'buenosaires.craigslist.org', 'lapaz.craigslist.org', 'belohorizonte.craigslist.org', '', 'brasilia.craigslist.org', '', 'curitiba.craigslist.org', '', 'fortaleza.craigslist.org', 'portoalegre.craigslist.org', 'recife.craigslist.org', 'rio.craigslist.org', 'salvador.craigslist.org', '', 'saopaulo.craigslist.org', 'caribbean.craigslist.org', 'santiago.craigslist.org', '', 'colombia.craigslist.org', '', 'costarica.craigslist.org', '', 'santodomingo.craigslist.org', '', 'quito.craigslist.org', '', 'elsalvador.craigslist.org', '', 'guatemala.craigslist.org', '', 'acapulco.craigslist.com.mx', '', 'bajasur.craigslist.com.mx', '', 'chihuahua.craigslist.com.mx', 'juarez.craigslist.com.mx', 'guadalajara.craigslist.com.mx', 'guanajuato.craigslist.com.mx', 'hermosillo.craigslist.com.mx', 'mazatlan.craigslist.com.mx', 'mexicocity.craigslist.com.mx', 'monterrey.craigslist.com.mx', 'oaxaca.craigslist.com.mx', 'puebla.craigslist.com.mx', 'pv.craigslist.com.mx', 'tijuana.craigslist.com.mx', 'veracruz.craigslist.com.mx', 'yucatan.craigslist.com.mx', 'managua.craigslist.org', 'panama.craigslist.org', '', 'lima.craigslist.org', '', 'puertorico.craigslist.org', '', 'montevideo.craigslist.org', '', 'caracas.craigslist.org', '', 'virgin.craigslist.org', '', 'cairo.craigslist.org', '', 'addisababa.craigslist.org', 'accra.craigslist.org', '', 'kenya.craigslist.org', '', 'casablanca.craigslist.org', '', 'capetown.craigslist.co.za', '', 'durban.craigslist.co.za', '', 'johannesburg.craigslist.co.za', '', 'pretoria.craigslist.co.za', 'tunis.craigslist.org', '', '', '', '']
# links = ['auburn.craigslist.org', 'bham.craigslist.org', 'dothan.craigslist.org', 'shoals.craigslist.org',
#          'gadsden.craigslist.org', 'huntsville.craigslist.org', 'mobile.craigslist.org', 'montgomery.craigslist.org',
#          'tuscaloosa.craigslist.org', 'anchorage.craigslist.org', 'fairbanks.craigslist.org', 'kenai.craigslist.org',
#          'juneau.craigslist.org', 'flagstaff.craigslist.org', 'mohave.craigslist.org', 'phoenix.craigslist.org',
#          'prescott.craigslist.org', 'showlow.craigslist.org', 'sierravista.craigslist.org', 'tucson.craigslist.org',
#          'yuma.craigslist.org', 'fayar.craigslist.org', 'fortsmith.craigslist.org', 'jonesboro.craigslist.org',
#          'littlerock.craigslist.org', 'texarkana.craigslist.org', 'bakersfield.craigslist.org', 'chico.craigslist.org',
#          'fresno.craigslist.org', 'goldcountry.craigslist.org', 'hanford.craigslist.org', 'humboldt.craigslist.org',
#          'imperial.craigslist.org', 'inlandempire.craigslist.org', 'losangeles.craigslist.org',
#          'mendocino.craigslist.org', 'merced.craigslist.org', 'modesto.craigslist.org', 'monterey.craigslist.org',
#          'orangecounty.craigslist.org', 'palmsprings.craigslist.org', 'redding.craigslist.org',
#          'sacramento.craigslist.org', 'sandiego.craigslist.org', 'sfbay.craigslist.org', 'slo.craigslist.org',
#          'santabarbara.craigslist.org', 'santamaria.craigslist.org', 'siskiyou.craigslist.org',
#          'stockton.craigslist.org', 'susanville.craigslist.org', 'ventura.craigslist.org', 'visalia.craigslist.org',
#          'yubasutter.craigslist.org', 'boulder.craigslist.org', 'cosprings.craigslist.org', 'denver.craigslist.org',
#          'eastco.craigslist.org', 'fortcollins.craigslist.org', 'rockies.craigslist.org', 'pueblo.craigslist.org',
#          'westslope.craigslist.org', 'newlondon.craigslist.org', 'hartford.craigslist.org', 'newhaven.craigslist.org',
#          'nwct.craigslist.org', 'delaware.craigslist.org', 'washingtondc.craigslist.org',
#          '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fbrw', 'daytona.craigslist.org', 'keys.craigslist.org',
#          'fortlauderdale.craigslist.org', 'fortmyers.craigslist.org', 'gainesville.craigslist.org',
#          'cfl.craigslist.org', 'jacksonville.craigslist.org', 'lakeland.craigslist.org',
#          '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc', 'lakecity.craigslist.org', 'ocala.craigslist.org',
#          'okaloosa.craigslist.org', 'orlando.craigslist.org', 'panamacity.craigslist.org', 'pensacola.craigslist.org',
#          'sarasota.craigslist.org', 'miami.craigslist.org', 'spacecoast.craigslist.org', 'staugustine.craigslist.org',
#          'tallahassee.craigslist.org', 'tampa.craigslist.org', 'treasure.craigslist.org',
#          '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc', 'albanyga.craigslist.org', 'athensga.craigslist.org',
#          'atlanta.craigslist.org', 'augusta.craigslist.org', 'brunswick.craigslist.org', 'columbusga.craigslist.org',
#          'macon.craigslist.org', 'nwga.craigslist.org', 'savannah.craigslist.org', 'statesboro.craigslist.org',
#          'valdosta.craigslist.org', 'honolulu.craigslist.org', 'boise.craigslist.org', 'eastidaho.craigslist.org',
#          'lewiston.craigslist.org', 'twinfalls.craigslist.org', 'bn.craigslist.org', 'chambana.craigslist.org',
#          'chicago.craigslist.org', 'decatur.craigslist.org', 'lasalle.craigslist.org', 'mattoon.craigslist.org',
#          'peoria.craigslist.org', 'rockford.craigslist.org', 'carbondale.craigslist.org',
#          'springfieldil.craigslist.org', 'quincy.craigslist.org', 'bloomington.craigslist.org',
#          'evansville.craigslist.org', 'fortwayne.craigslist.org', 'indianapolis.craigslist.org',
#          'kokomo.craigslist.org', 'tippecanoe.craigslist.org', 'muncie.craigslist.org', 'richmondin.craigslist.org',
#          'southbend.craigslist.org', 'terrehaute.craigslist.org', 'ames.craigslist.org', 'cedarrapids.craigslist.org',
#          'desmoines.craigslist.org', 'dubuque.craigslist.org', 'fortdodge.craigslist.org', 'iowacity.craigslist.org',
#          'masoncity.craigslist.org', 'quadcities.craigslist.org', 'siouxcity.craigslist.org', 'ottumwa.craigslist.org',
#          'waterloo.craigslist.org', 'lawrence.craigslist.org', 'ksu.craigslist.org', 'nwks.craigslist.org',
#          'salina.craigslist.org', 'seks.craigslist.org', 'swks.craigslist.org', 'topeka.craigslist.org',
#          'wichita.craigslist.org', 'bgky.craigslist.org', 'eastky.craigslist.org', 'lexington.craigslist.org',
#          'louisville.craigslist.org', 'owensboro.craigslist.org', 'westky.craigslist.org', 'batonrouge.craigslist.org',
#          'cenla.craigslist.org', 'houma.craigslist.org', 'lafayette.craigslist.org', 'lakecharles.craigslist.org',
#          'monroe.craigslist.org', 'neworleans.craigslist.org', 'shreveport.craigslist.org', 'maine.craigslist.org',
#          'annapolis.craigslist.org', 'baltimore.craigslist.org', 'easternshore.craigslist.org',
#          'frederick.craigslist.org', 'smd.craigslist.org', 'westmd.craigslist.org', 'boston.craigslist.org',
#          'capecod.craigslist.org', 'southcoast.craigslist.org', 'westernmass.craigslist.org',
#          'worcester.craigslist.org', 'annarbor.craigslist.org', 'battlecreek.craigslist.org',
#          'centralmich.craigslist.org', 'detroit.craigslist.org', 'flint.craigslist.org', 'grandrapids.craigslist.org',
#          'holland.craigslist.org', 'jxn.craigslist.org', 'kalamazoo.craigslist.org', 'lansing.craigslist.org',
#          'monroemi.craigslist.org', 'muskegon.craigslist.org', 'nmi.craigslist.org', 'porthuron.craigslist.org',
#          'saginaw.craigslist.org', 'swmi.craigslist.org', 'thumb.craigslist.org', 'up.craigslist.org',
#          'bemidji.craigslist.org', 'brainerd.craigslist.org', 'duluth.craigslist.org', 'mankato.craigslist.org',
#          'minneapolis.craigslist.org', 'rmn.craigslist.org', 'marshall.craigslist.org', 'stcloud.craigslist.org',
#          'gulfport.craigslist.org', 'hattiesburg.craigslist.org', 'jackson.craigslist.org', 'meridian.craigslist.org',
#          'northmiss.craigslist.org', 'natchez.craigslist.org', 'columbiamo.craigslist.org', 'joplin.craigslist.org',
#          'kansascity.craigslist.org', 'kirksville.craigslist.org', 'loz.craigslist.org', 'semo.craigslist.org',
#          'springfield.craigslist.org', 'stjoseph.craigslist.org', 'stlouis.craigslist.org', 'billings.craigslist.org',
#          'bozeman.craigslist.org', 'butte.craigslist.org', 'greatfalls.craigslist.org', 'helena.craigslist.org',
#          'kalispell.craigslist.org', 'missoula.craigslist.org', 'montana.craigslist.org', 'grandisland.craigslist.org',
#          'lincoln.craigslist.org', 'northplatte.craigslist.org', 'omaha.craigslist.org', 'scottsbluff.craigslist.org',
#          'elko.craigslist.org', 'lasvegas.craigslist.org', 'reno.craigslist.org', 'nh.craigslist.org',
#          'cnj.craigslist.org', 'jerseyshore.craigslist.org', 'newjersey.craigslist.org', 'southjersey.craigslist.org',
#          'albuquerque.craigslist.org', 'clovis.craigslist.org', 'farmington.craigslist.org', 'lascruces.craigslist.org',
#          'roswell.craigslist.org', 'santafe.craigslist.org', 'albany.craigslist.org', 'binghamton.craigslist.org',
#          'buffalo.craigslist.org', 'catskills.craigslist.org', 'chautauqua.craigslist.org', 'elmira.craigslist.org',
#          'fingerlakes.craigslist.org', 'glensfalls.craigslist.org', 'hudsonvalley.craigslist.org',
#          'ithaca.craigslist.org', 'longisland.craigslist.org', 'newyork.craigslist.org', 'oneonta.craigslist.org',
#          'plattsburgh.craigslist.org', 'potsdam.craigslist.org', 'rochester.craigslist.org', 'syracuse.craigslist.org',
#          'twintiers.craigslist.org', 'utica.craigslist.org', 'watertown.craigslist.org', 'asheville.craigslist.org',
#          'boone.craigslist.org', 'charlotte.craigslist.org', 'eastnc.craigslist.org', 'fayetteville.craigslist.org',
#          'greensboro.craigslist.org', 'hickory.craigslist.org', 'onslow.craigslist.org', 'outerbanks.craigslist.org',
#          'raleigh.craigslist.org', 'wilmington.craigslist.org', 'winstonsalem.craigslist.org',
#          'bismarck.craigslist.org', 'fargo.craigslist.org', 'grandforks.craigslist.org', 'nd.craigslist.org',
#          'akroncanton.craigslist.org', 'ashtabula.craigslist.org', 'athensohio.craigslist.org',
#          'chillicothe.craigslist.org', 'cincinnati.craigslist.org', 'cleveland.craigslist.org',
#          'columbus.craigslist.org', 'dayton.craigslist.org', 'limaohio.craigslist.org', 'mansfield.craigslist.org',
#          'sandusky.craigslist.org', 'toledo.craigslist.org', 'tuscarawas.craigslist.org', 'youngstown.craigslist.org',
#          'zanesville.craigslist.org', 'lawton.craigslist.org', 'enid.craigslist.org', 'oklahomacity.craigslist.org',
#          'stillwater.craigslist.org', 'tulsa.craigslist.org', 'bend.craigslist.org', 'corvallis.craigslist.org',
#          'eastoregon.craigslist.org', 'eugene.craigslist.org', 'klamath.craigslist.org', 'medford.craigslist.org',
#          'oregoncoast.craigslist.org', 'portland.craigslist.org', 'roseburg.craigslist.org', 'salem.craigslist.org',
#          'altoona.craigslist.org', 'chambersburg.craigslist.org', 'erie.craigslist.org', 'harrisburg.craigslist.org',
#          'lancaster.craigslist.org', 'allentown.craigslist.org', 'meadville.craigslist.org',
#          'philadelphia.craigslist.org', 'pittsburgh.craigslist.org', 'poconos.craigslist.org', 'reading.craigslist.org',
#          'scranton.craigslist.org', 'pennstate.craigslist.org', 'williamsport.craigslist.org', 'york.craigslist.org',
#          'providence.craigslist.org', 'charleston.craigslist.org', 'columbia.craigslist.org',
#          'florencesc.craigslist.org', 'greenville.craigslist.org', 'hiltonhead.craigslist.org',
#          'myrtlebeach.craigslist.org', 'nesd.craigslist.org', 'csd.craigslist.org', 'rapidcity.craigslist.org',
#          'siouxfalls.craigslist.org', 'sd.craigslist.org', 'chattanooga.craigslist.org', 'clarksville.craigslist.org',
#          'cookeville.craigslist.org', 'jacksontn.craigslist.org', 'knoxville.craigslist.org', 'memphis.craigslist.org',
#          'nashville.craigslist.org', 'tricities.craigslist.org', 'abilene.craigslist.org', 'amarillo.craigslist.org',
#          'austin.craigslist.org', 'beaumont.craigslist.org', 'brownsville.craigslist.org',
#          'collegestation.craigslist.org', 'corpuschristi.craigslist.org', 'dallas.craigslist.org',
#          'nacogdoches.craigslist.org', 'delrio.craigslist.org', 'elpaso.craigslist.org', 'galveston.craigslist.org',
#          'houston.craigslist.org', 'killeen.craigslist.org', 'laredo.craigslist.org', 'lubbock.craigslist.org',
#          'mcallen.craigslist.org', 'odessa.craigslist.org', 'sanangelo.craigslist.org', 'sanantonio.craigslist.org',
#          'sanmarcos.craigslist.org', 'bigbend.craigslist.org', 'texoma.craigslist.org', 'easttexas.craigslist.org',
#          'victoriatx.craigslist.org', 'waco.craigslist.org', 'wichitafalls.craigslist.org', 'logan.craigslist.org',
#          'ogden.craigslist.org', 'provo.craigslist.org', 'saltlakecity.craigslist.org', 'stgeorge.craigslist.org',
#          'vermont.craigslist.org', 'charlottesville.craigslist.org', 'danville.craigslist.org',
#          'fredericksburg.craigslist.org', 'norfolk.craigslist.org', 'harrisonburg.craigslist.org',
#          'lynchburg.craigslist.org', 'blacksburg.craigslist.org', 'richmond.craigslist.org', 'roanoke.craigslist.org',
#          'swva.craigslist.org', 'winchester.craigslist.org', 'bellingham.craigslist.org', 'kpr.craigslist.org',
#          'moseslake.craigslist.org', 'olympic.craigslist.org', 'pullman.craigslist.org', 'seattle.craigslist.org',
#          'skagit.craigslist.org', 'spokane.craigslist.org', 'wenatchee.craigslist.org', 'yakima.craigslist.org',
#          'charlestonwv.craigslist.org', 'martinsburg.craigslist.org', 'huntington.craigslist.org',
#          'morgantown.craigslist.org', 'wheeling.craigslist.org', 'parkersburg.craigslist.org', 'swv.craigslist.org',
#          'wv.craigslist.org', 'appleton.craigslist.org', 'eauclaire.craigslist.org', 'greenbay.craigslist.org',
#          'janesville.craigslist.org', 'racine.craigslist.org', 'lacrosse.craigslist.org', 'madison.craigslist.org',
#          'milwaukee.craigslist.org', 'northernwi.craigslist.org', 'sheboygan.craigslist.org', 'wausau.craigslist.org',
#          'wyoming.craigslist.org', 'micronesia.craigslist.org', 'puertorico.craigslist.org', 'virgin.craigslist.org',
#          'calgary.craigslist.org', 'edmonton.craigslist.org', 'ftmcmurray.craigslist.org', 'lethbridge.craigslist.org',
#          'hat.craigslist.org', 'peace.craigslist.org', 'reddeer.craigslist.org', 'cariboo.craigslist.org',
#          'comoxvalley.craigslist.org', 'abbotsford.craigslist.org', 'kamloops.craigslist.org', 'kelowna.craigslist.org',
#          'kootenays.craigslist.org', 'nanaimo.craigslist.org', 'princegeorge.craigslist.org', 'skeena.craigslist.org',
#          'sunshine.craigslist.org', 'vancouver.craigslist.org', 'victoria.craigslist.org', 'whistler.craigslist.org',
#          'winnipeg.craigslist.org', 'newbrunswick.craigslist.org', 'newfoundland.craigslist.org',
#          'territories.craigslist.org', 'yellowknife.craigslist.org', 'halifax.craigslist.org', 'barrie.craigslist.org',
#          'belleville.craigslist.org', 'brantford.craigslist.org', 'chatham.craigslist.org', 'cornwall.craigslist.org',
#          'guelph.craigslist.org', 'hamilton.craigslist.org', 'kingston.craigslist.org', 'kitchener.craigslist.org',
#          'londonon.craigslist.org', 'niagara.craigslist.org', 'ottawa.craigslist.org', 'owensound.craigslist.org',
#          'peterborough.craigslist.org', 'sarnia.craigslist.org', 'soo.craigslist.org', 'sudbury.craigslist.org',
#          'thunderbay.craigslist.org', 'toronto.craigslist.org', 'windsor.craigslist.org', 'pei.craigslist.org',
#          'montreal.craigslist.org', 'quebec.craigslist.org', 'saguenay.craigslist.org', 'sherbrooke.craigslist.org',
#          'troisrivieres.craigslist.org', 'regina.craigslist.org', 'saskatoon.craigslist.org',
#          'whitehorse.craigslist.org', 'vienna.craigslist.at', 'brussels.craigslist.org', 'bulgaria.craigslist.org',
#          'zagreb.craigslist.org', 'prague.craigslist.cz', 'copenhagen.craigslist.org', 'helsinki.craigslist.fi',
#          'bordeaux.craigslist.org', 'rennes.craigslist.org', 'grenoble.craigslist.org', 'lille.craigslist.org',
#          'loire.craigslist.org', 'lyon.craigslist.org', 'marseilles.craigslist.org', 'montpellier.craigslist.org',
#          'cotedazur.craigslist.org', 'rouen.craigslist.org', 'paris.craigslist.org', 'strasbourg.craigslist.org',
#          'toulouse.craigslist.org', 'berlin.craigslist.de', 'bremen.craigslist.de', 'cologne.craigslist.de',
#          'dresden.craigslist.de', 'dusseldorf.craigslist.de', 'essen.craigslist.de', 'frankfurt.craigslist.de',
#          'hamburg.craigslist.de', 'hannover.craigslist.de', 'heidelberg.craigslist.de', 'kaiserslautern.craigslist.de',
#          'leipzig.craigslist.de', 'munich.craigslist.de', 'nuremberg.craigslist.de', 'stuttgart.craigslist.de',
#          'athens.craigslist.gr', 'budapest.craigslist.org', 'reykjavik.craigslist.org', 'dublin.craigslist.org',
#          'bologna.craigslist.it', 'florence.craigslist.it', 'genoa.craigslist.it', 'milan.craigslist.it',
#          'naples.craigslist.it', 'perugia.craigslist.it', 'rome.craigslist.it', 'sardinia.craigslist.it',
#          'sicily.craigslist.it', 'torino.craigslist.it', 'venice.craigslist.it', 'luxembourg.craigslist.org',
#          'amsterdam.craigslist.org', 'oslo.craigslist.org', 'warsaw.craigslist.pl', 'faro.craigslist.pt',
#          'lisbon.craigslist.pt', 'porto.craigslist.pt', 'bucharest.craigslist.org', 'moscow.craigslist.org',
#          'stpetersburg.craigslist.org', 'alicante.craigslist.es', 'baleares.craigslist.es', 'barcelona.craigslist.es',
#          'bilbao.craigslist.es', 'cadiz.craigslist.es', 'canarias.craigslist.es', 'granada.craigslist.es',
#          'madrid.craigslist.es', 'malaga.craigslist.es', 'sevilla.craigslist.es', 'valencia.craigslist.es',
#          'stockholm.craigslist.se', 'basel.craigslist.ch', 'bern.craigslist.ch', 'geneva.craigslist.ch',
#          'lausanne.craigslist.ch', 'zurich.craigslist.ch', 'istanbul.craigslist.com.tr', 'ukraine.craigslist.org',
#          'aberdeen.craigslist.co.uk', 'bath.craigslist.co.uk', 'belfast.craigslist.co.uk',
#          'birmingham.craigslist.co.uk', 'brighton.craigslist.co.uk', 'bristol.craigslist.co.uk',
#          'cambridge.craigslist.co.uk', 'cardiff.craigslist.co.uk', 'coventry.craigslist.co.uk',
#          'derby.craigslist.co.uk', 'devon.craigslist.co.uk', 'dundee.craigslist.co.uk', 'norwich.craigslist.co.uk',
#          'eastmids.craigslist.co.uk', 'edinburgh.craigslist.co.uk', 'essex.craigslist.co.uk',
#          'glasgow.craigslist.co.uk', 'hampshire.craigslist.co.uk', 'kent.craigslist.co.uk', 'leeds.craigslist.co.uk',
#          'liverpool.craigslist.co.uk', 'london.craigslist.co.uk', 'manchester.craigslist.co.uk',
#          'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk', 'oxford.craigslist.co.uk',
#          'sheffield.craigslist.co.uk', 'bangladesh.craigslist.org', 'beijing.craigslist.com.cn',
#          'chengdu.craigslist.com.cn', 'chongqing.craigslist.com.cn', 'dalian.craigslist.com.cn',
#          'guangzhou.craigslist.com.cn', 'hangzhou.craigslist.com.cn', 'nanjing.craigslist.com.cn',
#          'shanghai.craigslist.com.cn', 'shenyang.craigslist.com.cn', 'shenzhen.craigslist.com.cn',
#          'wuhan.craigslist.com.cn', 'xian.craigslist.com.cn', 'micronesia.craigslist.org', 'hongkong.craigslist.hk',
#          'ahmedabad.craigslist.co.in', 'bangalore.craigslist.co.in', 'bhubaneswar.craigslist.co.in',
#          'chandigarh.craigslist.co.in', 'chennai.craigslist.co.in', 'delhi.craigslist.co.in', 'goa.craigslist.co.in',
#          'hyderabad.craigslist.co.in', 'indore.craigslist.co.in', 'jaipur.craigslist.co.in', 'kerala.craigslist.co.in',
#          'kolkata.craigslist.co.in', 'lucknow.craigslist.co.in', 'mumbai.craigslist.co.in', 'pune.craigslist.co.in',
#          'surat.craigslist.co.in', 'jakarta.craigslist.org', 'tehran.craigslist.org', 'baghdad.craigslist.org',
#          'haifa.craigslist.org', 'jerusalem.craigslist.org', 'telaviv.craigslist.org', 'ramallah.craigslist.org',
#          'fukuoka.craigslist.jp', 'hiroshima.craigslist.jp', 'nagoya.craigslist.jp', 'okinawa.craigslist.jp',
#          'osaka.craigslist.jp', 'sapporo.craigslist.jp', 'sendai.craigslist.jp', 'tokyo.craigslist.jp',
#          'seoul.craigslist.co.kr', 'kuwait.craigslist.org', 'beirut.craigslist.org', 'malaysia.craigslist.org',
#          'pakistan.craigslist.org', 'bacolod.craigslist.com.ph', 'naga.craigslist.com.ph', 'cdo.craigslist.com.ph',
#          'cebu.craigslist.com.ph', 'davaocity.craigslist.com.ph', 'iloilo.craigslist.com.ph',
#          'manila.craigslist.com.ph', 'pampanga.craigslist.com.ph', 'zamboanga.craigslist.com.ph',
#          'singapore.craigslist.com.sg', 'taipei.craigslist.com.tw', 'bangkok.craigslist.co.th', 'dubai.craigslist.org',
#          'vietnam.craigslist.org', 'adelaide.craigslist.com.au', 'brisbane.craigslist.com.au',
#          'cairns.craigslist.com.au', 'canberra.craigslist.com.au', 'darwin.craigslist.com.au',
#          'goldcoast.craigslist.com.au', 'melbourne.craigslist.com.au', 'ntl.craigslist.com.au',
#          'perth.craigslist.com.au', 'sydney.craigslist.com.au', 'hobart.craigslist.com.au',
#          'wollongong.craigslist.com.au', 'auckland.craigslist.org', 'christchurch.craigslist.org',
#          'dunedin.craigslist.co.nz', 'wellington.craigslist.org', 'buenosaires.craigslist.org', 'lapaz.craigslist.org',
#          'belohorizonte.craigslist.org', 'brasilia.craigslist.org', 'curitiba.craigslist.org',
#          'fortaleza.craigslist.org', 'portoalegre.craigslist.org', 'recife.craigslist.org', 'rio.craigslist.org',
#          'salvador.craigslist.org', 'saopaulo.craigslist.org', 'caribbean.craigslist.org', 'santiago.craigslist.org',
#          'colombia.craigslist.org', 'costarica.craigslist.org', 'santodomingo.craigslist.org', 'quito.craigslist.org',
#          'elsalvador.craigslist.org', 'guatemala.craigslist.org', 'acapulco.craigslist.com.mx',
#          'bajasur.craigslist.com.mx', 'chihuahua.craigslist.com.mx', 'juarez.craigslist.com.mx',
#          'guadalajara.craigslist.com.mx', 'guanajuato.craigslist.com.mx', 'hermosillo.craigslist.com.mx',
#          'mazatlan.craigslist.com.mx', 'mexicocity.craigslist.com.mx', 'monterrey.craigslist.com.mx',
#          'oaxaca.craigslist.com.mx', 'puebla.craigslist.com.mx', 'pv.craigslist.com.mx', 'tijuana.craigslist.com.mx',
#          'veracruz.craigslist.com.mx', 'yucatan.craigslist.com.mx', 'managua.craigslist.org', 'panama.craigslist.org',
#          'lima.craigslist.org', 'puertorico.craigslist.org', 'montevideo.craigslist.org', 'caracas.craigslist.org',
#          'virgin.craigslist.org', 'cairo.craigslist.org', 'addisababa.craigslist.org', 'accra.craigslist.org',
#          'kenya.craigslist.org', 'casablanca.craigslist.org', 'capetown.craigslist.co.za', 'durban.craigslist.co.za',
#          'johannesburg.craigslist.co.za', 'pretoria.craigslist.co.za', 'tunis.craigslist.org']
# link_texts = ['US', 'ALABAMA', 'Auburn', 'Birmingham', 'Dothan', 'Florence / Muscle Shoals', 'Gadsden-Anniston', 'Huntsville / Decatur', 'Mobile', 'Montgomery', 'Tuscaloosa', 'ALASKA', 'Anchorage / Mat-Su', 'Fairbanks', 'Kenai Peninsula', 'Southeast Alaska', 'ARIZONA', 'Flagstaff / Sedona', 'Mohave County', 'Phoenix', 'Prescott', 'Show Low', 'Sierra Vista', 'Tucson', 'Yuma', 'ARKANSAS', 'Fayetteville ', 'Fort Smith', 'Jonesboro', 'Little Rock', 'Texarkana', 'CALIFORNIA', 'Bakersfield', 'Chico', 'Fresno / Madera', 'Gold Country', 'Hanford-Corcoran', 'Humboldt County', 'Imperial County', 'Inland Empire', 'Los Angeles', 'Mendocino County', 'Merced', 'Modesto', 'Monterey Bay', 'Orange County', 'Palm Springs', 'Redding', 'Sacramento', 'San Diego', 'San Francisco Bay Area', 'San Luis Obispo', 'Santa Barbara', 'Santa Maria', 'Siskiyou County', 'Stockton', 'Susanville', 'Ventura County', 'Visalia-Tulare', 'Yuba-Sutter', 'COLORADO', 'Boulder', 'Colorado Springs', 'Denver', 'Eastern CO', 'Fort Collins / North CO', 'High Rockies', 'Pueblo', 'Western Slope', 'CONNECTICUT', 'Eastern CT', 'Hartford', 'New Haven', 'Northwest Ct', 'DELAWARE', 'Delaware', 'DISTRICT OF COLUMBIA', 'Washington', 'FLORIDA', 'Broward County', 'Daytona Beach', 'Florida Keys', 'Fort Lauderdale', 'Ft Myers / Sw Florida', 'Gainesville', 'Heartland Florida', 'Jacksonville', 'Lakeland', 'Miami / Dade', 'North Central FL', 'Ocala', 'Okaloosa / Walton', 'Orlando', 'Panama City', 'Pensacola', 'Sarasota-Bradenton', 'South Florida', 'Space Coast', 'St Augustine', 'Tallahassee', 'Tampa Bay Area', 'Treasure Coast', 'Palm Beach County', 'GEORGIA', 'Albany ', 'Athens', 'Atlanta', 'Augusta', 'Brunswick', 'Columbus ', 'Macon / Warner Robins', 'Northwest GA', 'Savannah / Hinesville', 'Statesboro', 'Valdosta', 'HAWAII', 'Hawaii', 'IDAHO', 'Boise', 'East Idaho', 'Lewiston / Clarkston', 'Twin Falls', 'ILLINOIS', 'Bloomington-Normal', 'Champaign Urbana', 'Chicago', 'Decatur', 'La Salle Co', 'Mattoon-Charleston', 'Peoria', 'Rockford', 'Southern Illinois', 'Springfield ', 'Western IL', 'INDIANA', 'Bloomington', 'Evansville', 'Fort Wayne', 'Indianapolis', 'Kokomo', 'Lafayette / West Lafayette', 'Muncie / Anderson', 'Richmond ', 'South Bend / Michiana', 'Terre Haute', 'IOWA', 'Ames', 'Cedar Rapids', 'Des Moines', 'Dubuque', 'Fort Dodge', 'Iowa City', 'Mason City', 'Quad Cities', 'Sioux City', 'Southeast IA', 'Waterloo / Cedar Falls', 'KANSAS', 'Lawrence', 'Manhattan', 'Northwest KS', 'Salina', 'Southeast KS', 'Southwest KS', 'Topeka', 'Wichita', 'KENTUCKY', 'Bowling Green', 'Eastern Kentucky', 'Lexington', 'Louisville', 'Owensboro', 'Western KY', 'LOUISIANA', 'Baton Rouge', 'Central Louisiana', 'Houma', 'Lafayette', 'Lake Charles', 'Monroe', 'New Orleans', 'Shreveport', 'MAINE', 'Maine', 'MARYLAND', 'Annapolis', 'Baltimore', 'Eastern Shore', 'Frederick', 'Southern Maryland', 'Western Maryland', 'MASSACHUSETTS', 'Boston', 'Cape Cod / Islands', 'South Coast', 'Western Massachusetts', 'Worcester / Central MA', 'MICHIGAN', 'Ann Arbor', 'Battle Creek', 'Central Michigan', 'Detroit Metro', 'Flint', 'Grand Rapids', 'Holland', 'Jackson ', 'Kalamazoo', 'Lansing', 'Monroe ', 'Muskegon', 'Northern Michigan', 'Port Huron', 'Saginaw-Midland-Baycity', 'Southwest Michigan', 'The Thumb', 'Upper Peninsula', 'MINNESOTA', 'Bemidji', 'Brainerd', 'Duluth / Superior', 'Mankato', 'Minneapolis / St Paul', 'Rochester ', 'Southwest MN', 'St Cloud', 'MISSISSIPPI', 'Gulfport / Biloxi', 'Hattiesburg', 'Jackson', 'Meridian', 'North Mississippi', 'Southwest MS', 'MISSOURI', 'Columbia / Jeff City', 'Joplin', 'Kansas City', 'Kirksville', 'Lake Of The Ozarks', 'Southeast Missouri', 'Springfield', 'St Joseph', 'St Louis', 'MONTANA', 'Billings', 'Bozeman', 'Butte', 'Great Falls', 'Helena', 'Kalispell', 'Missoula', 'Eastern Montana', 'NEBRASKA', 'Grand Island', 'Lincoln', 'North Platte', 'Omaha / Council Bluffs', 'Scottsbluff / Panhandle', 'NEVADA', 'Elko', 'Las Vegas', 'Reno / Tahoe', 'NEW HAMPSHIRE', 'New Hampshire', 'NEW JERSEY', 'Central NJ', 'Jersey Shore', 'North Jersey', 'South Jersey', 'NEW MEXICO', 'Albuquerque', 'Clovis / Portales', 'Farmington', 'Las Cruces', 'Roswell / Carlsbad', 'Santa Fe / Taos', 'NEW YORK', 'Albany', 'Binghamton', 'Buffalo', 'Catskills', 'Chautauqua', 'Elmira-Corning', 'Finger Lakes', 'Glens Falls', 'Hudson Valley', 'Ithaca', 'Long Island', 'New York City', 'Oneonta', 'Plattsburgh-Adirondacks', 'Potsdam-Canton-Massena', 'Rochester', 'Syracuse', 'Twin Tiers NY/PA', 'Utica-Rome-Oneida', 'Watertown', 'NORTH CAROLINA', 'Asheville', 'Boone', 'Charlotte', 'Eastern Nc', 'Fayetteville', 'Greensboro', 'Hickory / Lenoir', 'Jacksonville ', 'Outer Banks', 'Raleigh / Durham / CH', 'Wilmington', 'Winston-Salem', 'NORTH DAKOTA', 'Bismarck', 'Fargo / Moorhead', 'Grand Forks', 'North Dakota', 'OHIO', 'Akron / Canton', 'Ashtabula', 'Athens ', 'Chillicothe', 'Cincinnati', 'Cleveland', 'Columbus', 'Dayton / Springfield', 'Lima / Findlay', 'Mansfield', 'Sandusky', 'Toledo', 'Tuscarawas Co', 'Youngstown', 'Zanesville / Cambridge', 'OKLAHOMA', 'Lawton', 'Northwest OK', 'Oklahoma City', 'Stillwater', 'Tulsa', 'OREGON', 'Bend', 'Corvallis/Albany', 'East Oregon', 'Eugene', 'Klamath Falls', 'Medford-Ashland', 'Oregon Coast', 'Portland', 'Roseburg', 'Salem', 'PENNSYLVANIA', 'Altoona-Johnstown', 'Cumberland Valley', 'Erie', 'Harrisburg', 'Lancaster', 'Lehigh Valley', 'Meadville', 'Philadelphia', 'Pittsburgh', 'Poconos', 'Reading', 'Scranton / Wilkes-Barre', 'State College', 'Williamsport', 'York', 'RHODE ISLAND', 'Rhode Island', 'SOUTH CAROLINA', 'Charleston', 'Columbia', 'Florence', 'Greenville / Upstate', 'Hilton Head', 'Myrtle Beach', 'SOUTH DAKOTA', 'Northeast SD', 'Pierre / Central SD', 'Rapid City / West SD', 'Sioux Falls / Se SD', 'South Dakota', 'TENNESSEE', 'Chattanooga', 'Clarksville', 'Cookeville', 'Jackson  ', 'Knoxville', 'Memphis', 'Nashville', 'Tri-Cities', 'TEXAS', 'Abilene', 'Amarillo', 'Austin', 'Beaumont / Port Arthur', 'Brownsville', 'College Station', 'Corpus Christi', 'Dallas / Fort Worth', 'Deep East Texas', 'Del Rio / Eagle Pass', 'El Paso', 'Galveston', 'Houston', 'Killeen / Temple / Ft Hood', 'Laredo', 'Lubbock', 'Mcallen / Edinburg', 'Odessa / Midland', 'San Angelo', 'San Antonio', 'San Marcos', 'Southwest TX', 'Texoma', 'Tyler / East TX', 'Victoria ', 'Waco', 'Wichita Falls', 'UTAH', 'Logan', 'Ogden-Clearfield', 'Provo / Orem', 'Salt Lake City', 'St George', 'VERMONT', 'Vermont', 'VIRGINIA', 'Charlottesville', 'Danville', 'Fredericksburg', 'Hampton Roads', 'Harrisonburg', 'Lynchburg', 'New River Valley', 'Richmond', 'Roanoke', 'Southwest VA', 'Winchester', 'WASHINGTON', 'Bellingham', 'Kennewick-Pasco-Richland', 'Moses Lake', 'Olympic Peninsula', 'Pullman / Moscow', 'Seattle-Tacoma', 'Skagit / Island / SJI', "Spokane / Coeur D'Alene", 'Wenatchee', 'Yakima', 'WEST VIRGINIA', 'Charleston ', 'Eastern Panhandle', 'Huntington-Ashland', 'Morgantown', 'Northern Panhandle', 'Parkersburg-Marietta', 'Southern WV', 'West Virginia (Old)', 'WISCONSIN', 'Appleton-Oshkosh-FDL', 'Eau Claire', 'Green Bay', 'Janesville', 'Kenosha-Racine', 'La Crosse', 'Madison', 'Milwaukee', 'Northern Wi', 'Sheboygan', 'Wausau', 'WYOMING', 'Wyoming', 'TERRITORIES', 'Guam-Micronesia', 'Puerto Rico', 'U.S. Virgin Islands', 'CANADA', 'ALBERTA', 'Calgary', 'Edmonton', 'Ft Mcmurray', 'Lethbridge', 'Medicine Hat', 'Peace River Country', 'Red Deer', 'BRITISH COLUMBIA', 'Cariboo', 'Comox Valley', 'Fraser Valley', 'Kamloops', 'Kelowna / Okanagan', 'Kootenays', 'Nanaimo', 'Prince George', 'Skeena-Bulkley', 'Sunshine Coast', 'Vancouver', 'Victoria', 'Whistler', 'MANITOBA', 'Winnipeg', 'NEW BRUNSWICK', 'New Brunswick', 'NEWFOUNDLAND AND LABRADOR', "St John'S", 'NORTHWEST TERRITORIES', 'Territories', 'Yellowknife', 'NOVA SCOTIA', 'Halifax', 'ONTARIO', 'Barrie', 'Belleville', 'Brantford-Woodstock', 'Chatham-Kent', 'Cornwall', 'Guelph', 'Hamilton-Burlington', 'Kingston', 'Kitchener-Waterloo-Cambridge', 'London ', 'Niagara Region', 'Ottawa-Hull-Gatineau', 'Owen Sound', 'Peterborough', 'Sarnia', 'Sault Ste Marie', 'Sudbury', 'Thunder Bay', 'Toronto', 'Windsor', 'PRINCE EDWARD ISLAND', 'Prince Edward Island', 'QUEBEC', 'Montreal', 'Quebec City', 'Saguenay', 'Sherbrooke', 'Trois-Rivieres', 'SASKATCHEWAN', 'Regina', 'Saskatoon', 'YUKON TERRITORY', 'Whitehorse', 'EUROPE', 'AUSTRIA', 'Vienna', 'BELGIUM', 'Belgium', 'BULGARIA', 'Bulgaria', 'CROATIA', 'Croatia', 'CZECH REPUBLIC', 'Prague', 'DENMARK', 'Copenhagen', 'FINLAND', 'Finland', 'FRANCE', 'Bordeaux', 'Brittany', 'Grenoble', 'Lille', 'Loire Valley', 'Lyon', 'Marseille', 'Montpellier', "Nice / Cote D'Azur", 'Normandy', 'Paris', 'Strasbourg', 'Toulouse', 'GERMANY', 'Berlin', 'Bremen', 'Cologne', 'Dresden', 'Dusseldorf', 'Essen / Ruhr', 'Frankfurt', 'Hamburg', 'Hannover', 'Heidelberg', 'Kaiserslautern', 'Leipzig', 'Munich', 'Nuremberg', 'Stuttgart', 'GREECE', 'Greece', 'HUNGARY', 'Budapest', 'ICELAND', 'Reykjavik', 'IRELAND', 'Dublin', 'ITALY', 'Bologna', 'Florence / Tuscany', 'Genoa', 'Milan', 'Napoli / Campania', 'Perugia', 'Rome', 'Sardinia', 'Sicilia', 'Torino', 'Venice / Veneto', 'LUXEMBOURG', 'Luxembourg', 'NETHERLANDS', 'Amsterdam / Randstad', 'NORWAY', 'Norway', 'POLAND', 'Poland', 'PORTUGAL', 'Faro / Algarve', 'Lisbon', 'Porto', 'ROMANIA', 'Romania', 'RUSSIAN FEDERATION', 'Moscow', 'St Petersburg', 'SPAIN', 'Alicante', 'Baleares', 'Barcelona', 'Bilbao', 'Cadiz', 'Canarias', 'Granada', 'Madrid', 'Malaga', 'Sevilla', 'Valencia', 'SWEDEN', 'Sweden', 'SWITZERLAND', 'Basel', 'Bern', 'Geneva', 'Lausanne', 'Zurich', 'TURKEY', 'Turkey', 'UKRAINE', 'Ukraine', 'UNITED KINGDOM', 'Aberdeen', 'Bath', 'Belfast', 'Birmingham / West Mids', 'Brighton', 'Bristol', 'Cambridge, UK', 'Cardiff / Wales', 'Coventry', 'Derby', 'Devon & Cornwall', 'Dundee', 'East Anglia', 'East Midlands', 'Edinburgh', 'Essex', 'Glasgow', 'Hampshire', 'Kent', 'Leeds', 'Liverpool', 'London', 'Manchester', 'Newcastle / NE England', 'Nottingham', 'Oxford', 'Sheffield', 'ASIA, PACIFIC AND MIDDLE EAST', 'BANGLADESH', 'Bangladesh', 'CHINA', 'Beijing', 'Chengdu', 'Chongqing', 'Dalian', 'Guangzhou', 'Hangzhou', 'Nanjing', 'Shanghai', 'Shenyang', 'Shenzhen', 'Wuhan', "Xi'An", 'GUAM / MICRONESIA', 'Guam-Micronesia', 'HONG KONG', 'Hong Kong', 'INDIA', 'Ahmedabad', 'Bangalore', 'Bhubaneswar', 'Chandigarh', 'Chennai (Madras)', 'Delhi', 'Goa', 'Hyderabad', 'Indore', 'Jaipur', 'Kerala', 'Kolkata (Calcutta)', 'Lucknow', 'Mumbai', 'Pune', 'Surat Surat', 'INDONESIA', 'Indonesia', 'IRAN', 'Iran', 'IRAQ', 'Iraq', 'ISRAEL AND PALESTINE', 'Haifa', 'Jerusalem', 'Tel Aviv', 'West Bank', 'JAPAN', 'Fukuoka', 'Hiroshima', 'Nagoya', 'Okinawa', 'Osaka-Kobe-Kyoto', 'Sapporo', 'Sendai', 'Tokyo', 'KOREA', 'Seoul', 'KUWAIT', 'Kuwait', 'LEBANON', 'Beirut, Lebanon', 'MALAYSIA', 'Malaysia', 'PAKISTAN', 'Pakistan', 'PHILIPPINES', 'Bacolod', 'Bicol Region', 'Cagayan De Oro', 'Cebu', 'Davao City', 'Iloilo', 'Manila', 'Pampanga', 'Zamboanga', 'SINGAPORE', 'Singapore', 'TAIWAN', 'Taiwan', 'THAILAND', 'Thailand', 'UNITED ARAB EMIRATES', 'United Arab Emirates', 'VIETNAM', 'Vietnam', 'OCEANIA', 'AUSTRALIA', 'Adelaide', 'Brisbane', 'Cairns', 'Canberra', 'Darwin', 'Gold Coast', 'Melbourne', 'Newcastle, NSW', 'Perth', 'Sydney', 'Tasmania', 'Wollongong', 'NEW ZEALAND', 'Auckland', 'Christchurch', 'Dunedin', 'Wellington', 'LATIN AMERICA AND CARIBBEAN', 'ARGENTINA', 'Buenos Aires', 'BOLIVIA', 'Bolivia', 'BRAZIL', 'Belo Horizonte', 'Brasilia', 'Curitiba', 'Fortaleza', 'Porto Alegre', 'Recife', 'Rio De Janeiro', 'Salvador, Bahia', 'Sao Paulo', 'CARIBBEAN ISLANDS', 'Caribbean Islands', 'CHILE', 'Chile', 'COLOMBIA', 'Colombia', 'COSTA RICA', 'Costa Rica', 'DOMINICAN REPUBLIC', 'Dominican Republic', 'ECUADOR', 'Ecuador', 'EL SALVADOR', 'El Salvador', 'GUATEMALA', 'Guatemala', 'MEXICO', 'Acapulco', 'Baja California Sur', 'Chihuahua', 'Ciudad Juarez', 'Guadalajara', 'Guanajuato', 'Hermosillo', 'Mazatlan', 'Mexico City', 'Monterrey', 'Oaxaca', 'Puebla', 'Puerto Vallarta', 'Tijuana', 'Veracruz', 'Yucatan', 'NICARAGUA', 'Nicaragua', 'PANAMA', 'Panama', 'PERU', 'Peru', 'PUERTO RICO', 'Puerto Rico', 'URUGUAY', 'Montevideo', 'VENEZUELA', 'Venezuela', 'VIRGIN ISLANDS, U.S.', 'Virgin Islands', 'AFRICA', 'EGYPT', 'Egypt', 'ETHIOPIA', 'Ethiopia', 'GHANA', 'Ghana', 'KENYA', 'Kenya', 'MOROCCO', 'Morocco', 'SOUTH AFRICA', 'Cape Town', 'Durban', 'Johannesburg', 'Pretoria', 'TUNISIA', 'Tunisia']
# link_texts = ['US', 'Alabama', 'Auburn', 'Birmingham', 'Dothan', 'Florence / Muscle Shoals', 'Gadsden-Anniston', 'Huntsville / Decatur', 'Mobile', 'Montgomery', 'Tuscaloosa', 'Alaska', 'Anchorage / Mat-Su', 'Fairbanks', 'Kenai Peninsula', 'Southeast Alaska', 'Arizona', 'Flagstaff / Sedona', 'Mohave County', 'Phoenix', 'Prescott', 'Show Low', 'Sierra Vista', 'Tucson', 'Yuma', 'Arkansas', 'Fayetteville ', 'Fort Smith', 'Jonesboro', 'Little Rock', 'Texarkana', 'California', 'Bakersfield', 'Chico', 'Fresno / Madera', 'Gold Country', 'Hanford-Corcoran', 'Humboldt County', 'Imperial County', 'Inland Empire', 'Los Angeles', 'Mendocino County', 'Merced', 'Modesto', 'Monterey Bay', 'Orange County', 'Palm Springs', 'Redding', 'Sacramento', 'San Diego', 'San Francisco Bay Area', 'San Luis Obispo', 'Santa Barbara', 'Santa Maria', 'Siskiyou County', 'Stockton', 'Susanville', 'Ventura County', 'Visalia-Tulare', 'Yuba-Sutter', 'Colorado', 'Boulder', 'Colorado Springs', 'Denver', 'Eastern CO', 'Fort Collins / North CO', 'High Rockies', 'Pueblo', 'Western Slope', 'Connecticut', 'Eastern CT', 'Hartford', 'New Haven', 'Northwest Ct', 'Delaware', 'Delaware', 'District Of Columbia', 'Washington', 'Florida', 'Broward County', 'Daytona Beach', 'Florida Keys', 'Fort Lauderdale', 'Ft Myers / Sw Florida', 'Gainesville', 'Heartland Florida', 'Jacksonville', 'Lakeland', 'Miami / Dade', 'North Central FL', 'Ocala', 'Okaloosa / Walton', 'Orlando', 'Panama City', 'Pensacola', 'Sarasota-Bradenton', 'South Florida', 'Space Coast', 'St Augustine', 'Tallahassee', 'Tampa Bay Area', 'Treasure Coast', 'Palm Beach County', 'Georgia', 'Albany ', 'Athens', 'Atlanta', 'Augusta', 'Brunswick', 'Columbus ', 'Macon / Warner Robins', 'Northwest GA', 'Savannah / Hinesville', 'Statesboro', 'Valdosta', 'Hawaii', 'Hawaii', 'Idaho', 'Boise', 'East Idaho', 'Lewiston / Clarkston', 'Twin Falls', 'Illinois', 'Bloomington-Normal', 'Champaign Urbana', 'Chicago', 'Decatur', 'La Salle Co', 'Mattoon-Charleston', 'Peoria', 'Rockford', 'Southern Illinois', 'Springfield ', 'Western IL', 'Indiana', 'Bloomington', 'Evansville', 'Fort Wayne', 'Indianapolis', 'Kokomo', 'Lafayette / West Lafayette', 'Muncie / Anderson', 'Richmond ', 'South Bend / Michiana', 'Terre Haute', 'Iowa', 'Ames', 'Cedar Rapids', 'Des Moines', 'Dubuque', 'Fort Dodge', 'Iowa City', 'Mason City', 'Quad Cities', 'Sioux City', 'Southeast IA', 'Waterloo / Cedar Falls', 'Kansas', 'Lawrence', 'Manhattan', 'Northwest KS', 'Salina', 'Southeast KS', 'Southwest KS', 'Topeka', 'Wichita', 'Kentucky', 'Bowling Green', 'Eastern Kentucky', 'Lexington', 'Louisville', 'Owensboro', 'Western KY', 'Louisiana', 'Baton Rouge', 'Central Louisiana', 'Houma', 'Lafayette', 'Lake Charles', 'Monroe', 'New Orleans', 'Shreveport', 'Maine', 'Maine', 'Maryland', 'Annapolis', 'Baltimore', 'Eastern Shore', 'Frederick', 'Southern Maryland', 'Western Maryland', 'Massachusetts', 'Boston', 'Cape Cod / Islands', 'South Coast', 'Western Massachusetts', 'Worcester / Central MA', 'Michigan', 'Ann Arbor', 'Battle Creek', 'Central Michigan', 'Detroit Metro', 'Flint', 'Grand Rapids', 'Holland', 'Jackson ', 'Kalamazoo', 'Lansing', 'Monroe ', 'Muskegon', 'Northern Michigan', 'Port Huron', 'Saginaw-Midland-Baycity', 'Southwest Michigan', 'The Thumb', 'Upper Peninsula', 'Minnesota', 'Bemidji', 'Brainerd', 'Duluth / Superior', 'Mankato', 'Minneapolis / St Paul', 'Rochester ', 'Southwest MN', 'St Cloud', 'Mississippi', 'Gulfport / Biloxi', 'Hattiesburg', 'Jackson', 'Meridian', 'North Mississippi', 'Southwest MS', 'Missouri', 'Columbia / Jeff City', 'Joplin', 'Kansas City', 'Kirksville', 'Lake Of The Ozarks', 'Southeast Missouri', 'Springfield', 'St Joseph', 'St Louis', 'Montana', 'Billings', 'Bozeman', 'Butte', 'Great Falls', 'Helena', 'Kalispell', 'Missoula', 'Eastern Montana', 'Nebraska', 'Grand Island', 'Lincoln', 'North Platte', 'Omaha / Council Bluffs', 'Scottsbluff / Panhandle', 'Nevada', 'Elko', 'Las Vegas', 'Reno / Tahoe', 'New Hampshire', 'New Hampshire', 'New Jersey', 'Central NJ', 'Jersey Shore', 'North Jersey', 'South Jersey', 'New Mexico', 'Albuquerque', 'Clovis / Portales', 'Farmington', 'Las Cruces', 'Roswell / Carlsbad', 'Santa Fe / Taos', 'New York', 'Albany', 'Binghamton', 'Buffalo', 'Catskills', 'Chautauqua', 'Elmira-Corning', 'Finger Lakes', 'Glens Falls', 'Hudson Valley', 'Ithaca', 'Long Island', 'New York City', 'Oneonta', 'Plattsburgh-Adirondacks', 'Potsdam-Canton-Massena', 'Rochester', 'Syracuse', 'Twin Tiers NY/PA', 'Utica-Rome-Oneida', 'Watertown', 'North Carolina', 'Asheville', 'Boone', 'Charlotte', 'Eastern Nc', 'Fayetteville', 'Greensboro', 'Hickory / Lenoir', 'Jacksonville ', 'Outer Banks', 'Raleigh / Durham / CH', 'Wilmington', 'Winston-Salem', 'North Dakota', 'Bismarck', 'Fargo / Moorhead', 'Grand Forks', 'North Dakota', 'Ohio', 'Akron / Canton', 'Ashtabula', 'Athens ', 'Chillicothe', 'Cincinnati', 'Cleveland', 'Columbus', 'Dayton / Springfield', 'Lima / Findlay', 'Mansfield', 'Sandusky', 'Toledo', 'Tuscarawas Co', 'Youngstown', 'Zanesville / Cambridge', 'Oklahoma', 'Lawton', 'Northwest OK', 'Oklahoma City', 'Stillwater', 'Tulsa', 'Oregon', 'Bend', 'Corvallis/Albany', 'East Oregon', 'Eugene', 'Klamath Falls', 'Medford-Ashland', 'Oregon Coast', 'Portland', 'Roseburg', 'Salem', 'Pennsylvania', 'Altoona-Johnstown', 'Cumberland Valley', 'Erie', 'Harrisburg', 'Lancaster', 'Lehigh Valley', 'Meadville', 'Philadelphia', 'Pittsburgh', 'Poconos', 'Reading', 'Scranton / Wilkes-Barre', 'State College', 'Williamsport', 'York', 'Rhode Island', 'Rhode Island', 'South Carolina', 'Charleston', 'Columbia', 'Florence', 'Greenville / Upstate', 'Hilton Head', 'Myrtle Beach', 'South Dakota', 'Northeast SD', 'Pierre / Central SD', 'Rapid City / West SD', 'Sioux Falls / Se SD', 'South Dakota', 'Tennessee', 'Chattanooga', 'Clarksville', 'Cookeville', 'Jackson  ', 'Knoxville', 'Memphis', 'Nashville', 'Tri-Cities', 'Texas', 'Abilene', 'Amarillo', 'Austin', 'Beaumont / Port Arthur', 'Brownsville', 'College Station', 'Corpus Christi', 'Dallas / Fort Worth', 'Deep East Texas', 'Del Rio / Eagle Pass', 'El Paso', 'Galveston', 'Houston', 'Killeen / Temple / Ft Hood', 'Laredo', 'Lubbock', 'Mcallen / Edinburg', 'Odessa / Midland', 'San Angelo', 'San Antonio', 'San Marcos', 'Southwest TX', 'Texoma', 'Tyler / East TX', 'Victoria ', 'Waco', 'Wichita Falls', 'Utah', 'Logan', 'Ogden-Clearfield', 'Provo / Orem', 'Salt Lake City', 'St George', 'Vermont', 'Vermont', 'Virginia', 'Charlottesville', 'Danville', 'Fredericksburg', 'Hampton Roads', 'Harrisonburg', 'Lynchburg', 'New River Valley', 'Richmond', 'Roanoke', 'Southwest VA', 'Winchester', 'Washington', 'Bellingham', 'Kennewick-Pasco-Richland', 'Moses Lake', 'Olympic Peninsula', 'Pullman / Moscow', 'Seattle-Tacoma', 'Skagit / Island / SJI', "Spokane / Coeur D'Alene", 'Wenatchee', 'Yakima', 'West Virginia', 'Charleston ', 'Eastern Panhandle', 'Huntington-Ashland', 'Morgantown', 'Northern Panhandle', 'Parkersburg-Marietta', 'Southern WV', 'West Virginia (Old)', 'Wisconsin', 'Appleton-Oshkosh-FDL', 'Eau Claire', 'Green Bay', 'Janesville', 'Kenosha-Racine', 'La Crosse', 'Madison', 'Milwaukee', 'Northern Wi', 'Sheboygan', 'Wausau', 'Wyoming', 'Wyoming', 'Territories', 'Guam-Micronesia', 'Puerto Rico', 'U.S. Virgin Islands', 'CANADA', 'Alberta', 'Calgary', 'Edmonton', 'Ft Mcmurray', 'Lethbridge', 'Medicine Hat', 'Peace River Country', 'Red Deer', 'British Columbia', 'Cariboo', 'Comox Valley', 'Fraser Valley', 'Kamloops', 'Kelowna / Okanagan', 'Kootenays', 'Nanaimo', 'Prince George', 'Skeena-Bulkley', 'Sunshine Coast', 'Vancouver', 'Victoria', 'Whistler', 'Manitoba', 'Winnipeg', 'New Brunswick', 'New Brunswick', 'Newfoundland And Labrador', "St John'S", 'Northwest Territories', 'Territories', 'Yellowknife', 'Nova Scotia', 'Halifax', 'Ontario', 'Barrie', 'Belleville', 'Brantford-Woodstock', 'Chatham-Kent', 'Cornwall', 'Guelph', 'Hamilton-Burlington', 'Kingston', 'Kitchener-Waterloo-Cambridge', 'London ', 'Niagara Region', 'Ottawa-Hull-Gatineau', 'Owen Sound', 'Peterborough', 'Sarnia', 'Sault Ste Marie', 'Sudbury', 'Thunder Bay', 'Toronto', 'Windsor', 'Prince Edward Island', 'Prince Edward Island', 'Quebec', 'Montreal', 'Quebec City', 'Saguenay', 'Sherbrooke', 'Trois-Rivieres', 'Saskatchewan', 'Regina', 'Saskatoon', 'Yukon Territory', 'Whitehorse', 'EUROPE', 'Austria', 'Vienna', 'Belgium', 'Belgium', 'Bulgaria', 'Bulgaria', 'Croatia', 'Croatia', 'Czech Republic', 'Prague', 'Denmark', 'Copenhagen', 'Finland', 'Finland', 'France', 'Bordeaux', 'Brittany', 'Grenoble', 'Lille', 'Loire Valley', 'Lyon', 'Marseille', 'Montpellier', "Nice / Cote D'Azur", 'Normandy', 'Paris', 'Strasbourg', 'Toulouse', 'Germany', 'Berlin', 'Bremen', 'Cologne', 'Dresden', 'Dusseldorf', 'Essen / Ruhr', 'Frankfurt', 'Hamburg', 'Hannover', 'Heidelberg', 'Kaiserslautern', 'Leipzig', 'Munich', 'Nuremberg', 'Stuttgart', 'Greece', 'Greece', 'Hungary', 'Budapest', 'Iceland', 'Reykjavik', 'Ireland', 'Dublin', 'Italy', 'Bologna', 'Florence / Tuscany', 'Genoa', 'Milan', 'Napoli / Campania', 'Perugia', 'Rome', 'Sardinia', 'Sicilia', 'Torino', 'Venice / Veneto', 'Luxembourg', 'Luxembourg', 'Netherlands', 'Amsterdam / Randstad', 'Norway', 'Norway', 'Poland', 'Poland', 'Portugal', 'Faro / Algarve', 'Lisbon', 'Porto', 'Romania', 'Romania', 'Russian Federation', 'Moscow', 'St Petersburg', 'Spain', 'Alicante', 'Baleares', 'Barcelona', 'Bilbao', 'Cadiz', 'Canarias', 'Granada', 'Madrid', 'Malaga', 'Sevilla', 'Valencia', 'Sweden', 'Sweden', 'Switzerland', 'Basel', 'Bern', 'Geneva', 'Lausanne', 'Zurich', 'Turkey', 'Turkey', 'Ukraine', 'Ukraine', 'United Kingdom', 'Aberdeen', 'Bath', 'Belfast', 'Birmingham / West Mids', 'Brighton', 'Bristol', 'Cambridge, UK', 'Cardiff / Wales', 'Coventry', 'Derby', 'Devon & Cornwall', 'Dundee', 'East Anglia', 'East Midlands', 'Edinburgh', 'Essex', 'Glasgow', 'Hampshire', 'Kent', 'Leeds', 'Liverpool', 'London', 'Manchester', 'Newcastle / NE England', 'Nottingham', 'Oxford', 'Sheffield', 'ASIA, PACIFIC AND MIDDLE EAST', 'Bangladesh', 'Bangladesh', 'China', 'Beijing', 'Chengdu', 'Chongqing', 'Dalian', 'Guangzhou', 'Hangzhou', 'Nanjing', 'Shanghai', 'Shenyang', 'Shenzhen', 'Wuhan', "Xi'An", 'Guam / Micronesia', 'Guam-Micronesia', 'Hong Kong', 'Hong Kong', 'India', 'Ahmedabad', 'Bangalore', 'Bhubaneswar', 'Chandigarh', 'Chennai (Madras)', 'Delhi', 'Goa', 'Hyderabad', 'Indore', 'Jaipur', 'Kerala', 'Kolkata (Calcutta)', 'Lucknow', 'Mumbai', 'Pune', 'Surat Surat', 'Indonesia', 'Indonesia', 'Iran', 'Iran', 'Iraq', 'Iraq', 'Israel And Palestine', 'Haifa', 'Jerusalem', 'Tel Aviv', 'West Bank', 'Japan', 'Fukuoka', 'Hiroshima', 'Nagoya', 'Okinawa', 'Osaka-Kobe-Kyoto', 'Sapporo', 'Sendai', 'Tokyo', 'Korea', 'Seoul', 'Kuwait', 'Kuwait', 'Lebanon', 'Beirut, Lebanon', 'Malaysia', 'Malaysia', 'Pakistan', 'Pakistan', 'Philippines', 'Bacolod', 'Bicol Region', 'Cagayan De Oro', 'Cebu', 'Davao City', 'Iloilo', 'Manila', 'Pampanga', 'Zamboanga', 'Singapore', 'Singapore', 'Taiwan', 'Taiwan', 'Thailand', 'Thailand', 'United Arab Emirates', 'United Arab Emirates', 'Vietnam', 'Vietnam', 'OCEANIA', 'Australia', 'Adelaide', 'Brisbane', 'Cairns', 'Canberra', 'Darwin', 'Gold Coast', 'Melbourne', 'Newcastle, NSW', 'Perth', 'Sydney', 'Tasmania', 'Wollongong', 'New Zealand', 'Auckland', 'Christchurch', 'Dunedin', 'Wellington', 'LATIN AMERICA AND CARIBBEAN', 'Argentina', 'Buenos Aires', 'Bolivia', 'Bolivia', 'Brazil', 'Belo Horizonte', 'Brasilia', 'Curitiba', 'Fortaleza', 'Porto Alegre', 'Recife', 'Rio De Janeiro', 'Salvador, Bahia', 'Sao Paulo', 'Caribbean Islands', 'Caribbean Islands', 'Chile', 'Chile', 'Colombia', 'Colombia', 'Costa Rica', 'Costa Rica', 'Dominican Republic', 'Dominican Republic', 'Ecuador', 'Ecuador', 'El Salvador', 'El Salvador', 'Guatemala', 'Guatemala', 'Mexico', 'Acapulco', 'Baja California Sur', 'Chihuahua', 'Ciudad Juarez', 'Guadalajara', 'Guanajuato', 'Hermosillo', 'Mazatlan', 'Mexico City', 'Monterrey', 'Oaxaca', 'Puebla', 'Puerto Vallarta', 'Tijuana', 'Veracruz', 'Yucatan', 'Nicaragua', 'Nicaragua', 'Panama', 'Panama', 'Peru', 'Peru', 'Puerto Rico', 'Puerto Rico', 'Uruguay', 'Montevideo', 'Venezuela', 'Venezuela', 'Virgin Islands, U.S.', 'Virgin Islands', 'AFRICA', 'Egypt', 'Egypt', 'Ethiopia', 'Ethiopia', 'Ghana', 'Ghana', 'Kenya', 'Kenya', 'Morocco', 'Morocco', 'South Africa', 'Cape Town', 'Durban', 'Johannesburg', 'Pretoria', 'Tunisia', 'Tunisia']
# headers_pos = [0, 473, 541, 675, 762, 781, 843]
# sub_headers_pos = [1, 11, 16, 25, 31, 60, 69, 74, 76, 78, 103, 115, 117, 122, 134, 145, 157, 166, 173, 182, 184, 191, 197, 216, 225, 232, 242, 251, 257, 261, 263, 268, 275, 296, 309, 314, 330, 336, 347, 363, 365, 372, 378, 387, 415, 421, 423, 435, 446, 455, 467, 469, 474, 482, 496, 498, 500, 502, 505, 507, 528, 530, 536, 539, 542, 544, 546, 548, 550, 552, 554, 556, 570, 586, 588, 590, 592, 594, 606, 608, 610, 612, 614, 618, 620, 623, 635, 637, 643, 645, 647, 676, 678, 691, 693, 695, 712, 714, 716, 718, 723, 732, 734, 736, 738, 740, 742, 752, 754, 756, 758, 760, 763, 776, 782, 784, 786, 796, 798, 800, 802, 804, 806, 808, 810, 812, 829, 831, 833, 835, 837, 839, 841, 844, 846, 848, 850, 852, 854, 859]

# # # Hi Guys! Please can I be a part of your team?
# # # Am a Nigerian and I feel I have a lot to offer us!
# # #
# # # FIRST NAME: BASIT
# # # LAST NAME: BALOGUN
# # # AGE: 17
# # #
# # # I await your response, thanks!
# # # <iframe width="800" height="641" src="https://www.youtube.com/embed/WXPzqgb7fKI?list=PLgqiBpQGzC2D6HZUn9jetHvJUJgJ7lFkt" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# # # {
# # #   "ns": "yt",
# # #   "el": "embedded",
# # #   "cpn": "Dk-_IFJrxa_XOJuJ",
# # #   "docid": "WXPzqgb7fKI",
# # #   "ver": 2,
# # #   "cmt": "0",
# # #   "fs": "0",
# # #   "rt": "0.002",
# # #   "euri": "https://challenges.reply.com/",
# # #   "lact": 156,
# # #   "cl": "356830393",
# # #   "mos": 0,
# # #   "state": "40",
# # #   "volume": 100,
# # #   "cbr": "Chrome",
# # #   "cbrver": "88.0.4324.150",
# # #   "c": "WEB_EMBEDDED_PLAYER",
# # #   "cver": "1.20210210.1.0",
# # #   "cplayer": "UNIPLAYER",
# # #   "cos": "Windows",
# # #   "cosver": "10.0",
# # #   "cplatform": "DESKTOP",
# # #   "hl": "en_US",
# # #   "cr": "CZ",
# # #   "len": "0",
# # #   "fexp": "23857949,23969934,23976578,23987575,23988825,23996625,23997515,23998150,24631707",
# # #   "list": "PLgqiBpQGzC2D6HZUn9jetHvJUJgJ7lFkt",
# # #   "size": "800:641",
# # #   "inview": "0.81",
# # #   "vct": "0.000",
# # #   "vd": "NaN",
# # #   "vpl": "",
# # #   "vbu": "",
# # #   "vpa": "1",
# # #   "vsk": "0",
# # #   "ven": "0",
# # #   "vpr": "1",
# # #   "vrs": "0",
# # #   "vns": "0",
# # #   "vec": "null",
# # #   "vemsg": "",
# # #   "vvol": "1",
# # #   "vdom": "1",
# # #   "vsrc": "0",
# # #   "vw": "800",
# # #   "vh": "641",
# # #   "relative_loudness": "NaN",
# # #   "user_qual": "hd720",
# # #   "debug_videoId": "WXPzqgb7fKI",
# # #   "0sz": false,
# # #   "op": "",
# # #   "yof": true,
# # #   "dis": "",
# # #   "gpu": "ANGLE_(Mobile_Intel(R)_4_Series_Express_Chipset_Family_Direct3D9Ex_vs_3_0_ps_3_0)",
# # #   "cgr": true,
# # #   "debug_playbackQuality": "unknown",
# # #   "debug_date": "Fri Feb 12 2021 03:55:29 GMT+0100 (West Africa Standard Time)"
# # # }
# # # < div
# # #
# # #
# # # class ="container" >
# # #
# # # < div
# # #
# # #
# # # class ="row" >
# # #
# # # < div
# # #
# # #
# # # class ="col s12" >
# # #
# # # < div
# # #
# # #
# # # class ="right" >
# # #
# # # < h5 >
# # # < a
# # #
# # #
# # # class ='dropdown-button btn  pink accent-3' href='#' data-activates='sort_options' > Sort By < i class ="large material-icons" >
# # #
# # #
# # # arrow_drop_down < / i > < / a >
# # # < / h5 >
# # #
# # # < !-- Dropdown
# # # Structure -->
# # # < ul
# # # id = 'sort_options'
# # #
# # #
# # # class ='dropdown-content' >
# # #
# # # < !-- Define
# # # the
# # # links in the
# # # dropdown -->
# # # < li >
# # # < a
# # # href = "#!" > Relevant < / a >
# # # < / li >
# # # < li >
# # # < a
# # # href = "#!" > Newest < / a >
# # # < / li >
# # # < li >
# # # < a
# # # href = "#!" > < i
# # #
# # #
# # # class ="material-icons" > < / i > Price (Ascending) < / a >
# # #
# # # < / li >
# # # < li >
# # # < a
# # # href = "#!" > < i
# # #
# # #
# # # class ="material-icons" > < / i > Price (Descending) < / a >
# # #
# # # < / li >
# # # < / ul >
# # # < / div >
# # # < / div >
# # #
# # # < div
# # #
# # #
# # # class ="col s12" >
# # #
# # # < div
# # #
# # #
# # # class ="right" >
# # #
# # # < h5 >
# # # < a
# # #
# # #
# # # class ='dropdown-button btn  blue darken-4' href='#' data-activates='sections' > Sections < i class ="large material-icons" >
# # #
# # #
# # # arrow_drop_down < / i > < / a >
# # # < / h5 >
# # #
# # # < !-- Dropdown
# # # Structure -->
# # # < ul
# # # id = 'sections'
# # #
# # #
# # # class ='dropdown-content' >
# # #
# # # < !-- Define
# # # the
# # # links in the
# # # dropdown -->
# # # < li >
# # # < a
# # # href = "#!" > Community < / a >
# # # < / li >
# # # < li
# # #
# # #
# # # class ="divider" tabindex="-1" green accent-4 > < / li >
# # #
# # # < li >
# # # < a
# # # href = "#!" > Events < / a >
# # # < / li >
# # # < li
# # #
# # #
# # # class ="divider" tabindex="-1" green accent-4 > < / li >
# # #
# # # < li >
# # # < a
# # # href = "#!" > For
# # # Sale < / a >
# # # < / li >
# # # < li
# # #
# # #
# # # class ="divider" tabindex="-1" green accent-4 > < / li >
# # #
# # # < li >
# # # < a
# # # href = "#!" > Gigs < / a >
# # # < / li >
# # # < li
# # #
# # #
# # # class ="divider" tabindex="-1" green accent-4 > < / li >
# # #
# # # < li >
# # # < a
# # # href = "#!" > Housing < / a >
# # # < / li >
# # # < li
# # #
# # #
# # # class ="divider" tabindex="-1" green accent-4 > < / li >
# # #
# # # < li >
# # # < a
# # # href = "#!" > Jobs < / a >
# # # < / li >
# # # < li
# # #
# # #
# # # class ="divider" tabindex="-1" green accent-4 > < / li >
# # #
# # # < li >
# # # < a
# # # href = "#!" > Resumes < / a >
# # # < / li >
# # # < li
# # #
# # #
# # # class ="divider" tabindex="-1" green accent-4 > < / li >
# # #
# # # < li >
# # # < a
# # # href = "#!" > Services < / a >
# # # < / li >
# # # < / ul >
# # # < / div >
# # # < / div >
# # # < / div >
#
#
# # sum = 0
# # for number in range(1, 11):
# #     sum+=number
# # print(sum)
#
# # num = int(input("enter a number:  "))
# # fac = 1
# # for i in range(1, num + 1):
# #     fac*=i
# #     print(fac)
#
# # number = int(input("enter a number:  "))
# # fac = 1
# # count = 1
# # while number >= count:
# #     fac*=count
# #     count+=1
# # print("factorial of %d is %d" %(number, fac))
#
# # number = int(input("enter a number:  "))
# # for i in range(2, number):
# #     if number % i == 0:
# #         print("number is not a prime")
# #         break
# # else:
# #     print("number is a prime")
#
#
#
#
#
#
#

# print(help(zip))
# print(list(zip(range(4), range(6), range(2, 10))))

# ARITHMETIC PROGRESSION GENERATOR
# from random import random, randint, randrange
#
# for num in range(50):
#     ml = []
#     n = randint(7, 14)
#     a = randint(1, 100)
#     d = randint(1, 20)
#     q = randrange(n, 4, -1)
#     # print('number of terms: ', n)
#     # print('first term: ', a)
#     # print('common difference: ', d)
#
#     for num in range(n):
#         ml.append(a)
#         a += d
#
#     print(ml, n)
#     print('FIND TERM NUMBER: ', q)
#     print()
#     print()
#
# ARITHMETIC PROGRESSION GENERATOR ENDS

# name=''
# age=''
# score =''
#
# if name == '' and age == '' and score == '':
#     print('ALL EMPTY')
# else:
#     print('ALL NOT EMPTY')

# min
# md = {'': 'empty', 'name': 'basit', 'S':'empty2'}
# print(md)
#
# min_price = ''
# max_price = '4'
# min_bedroom = ''
# max_bedroom = '3'
# min_bathroom = ''
# max_bathroom = '4'
# link = 'losangeles.craigslist.org'
# section = 'housing'
# section_abb = 'hhh'
# sort_abb = 'rel'
# search = 'duplex'
#
# filters = {'&min_price={}': min_price, '&max_price={}': max_price, '&min_bedrooms={}': min_bedroom, '&max_bedrooms={}': max_bedroom, '&min_bathrooms={}': min_bathroom , '&max_bathrooms={}': max_bathroom}
# # print(filters)
# URL = 'https://{}/d/{}/search/{}?sort={}&query={}&min_price={}&max_price={}&min_bedrooms={}&max_bedrooms={}&min_bathrooms={}&max_bathrooms={}'
# formats = [link, section, section_abb, sort_abb, search, min_price, max_price, min_bedroom, max_bedroom, min_bathroom, max_bathroom]
# # print(''.join(URL.split('&min_price={}')))
#
# for frag, filt in filters.items():
#     if filt == '':
#         URL = URL.split(frag)
#         URL = ''.join(URL)
#         formats.remove(filt)
#
# print(formats)
# print(URL)
# pos = 0
# for braces in range(URL.find('{}')):
#     replacement = formats[pos]
#     URL = URL.replace('{}', formats[pos], 1)
#     pos += 1
#
# print(URL)
# final_url = URL.format(tuple(formats))
# print(final_url)

# links = ['', '', 'auburn.craigslist.org', 'bham.craigslist.org', 'dothan.craigslist.org', 'shoals.craigslist.org', 'gadsden.craigslist.org', 'huntsville.craigslist.org', 'mobile.craigslist.org', 'montgomery.craigslist.org', 'tuscaloosa.craigslist.org', '', 'anchorage.craigslist.org', 'fairbanks.craigslist.org', 'kenai.craigslist.org', 'juneau.craigslist.org', '', 'flagstaff.craigslist.org', 'mohave.craigslist.org', 'phoenix.craigslist.org', 'prescott.craigslist.org', 'showlow.craigslist.org', 'sierravista.craigslist.org', 'tucson.craigslist.org', 'yuma.craigslist.org', '', 'fayar.craigslist.org', 'fortsmith.craigslist.org', 'jonesboro.craigslist.org', 'littlerock.craigslist.org', 'texarkana.craigslist.org', '', 'bakersfield.craigslist.org', 'chico.craigslist.org', 'fresno.craigslist.org', 'goldcountry.craigslist.org', 'hanford.craigslist.org', 'humboldt.craigslist.org', 'imperial.craigslist.org', 'inlandempire.craigslist.org', 'losangeles.craigslist.org', 'mendocino.craigslist.org', 'merced.craigslist.org', 'modesto.craigslist.org', 'monterey.craigslist.org', 'orangecounty.craigslist.org', 'palmsprings.craigslist.org', 'redding.craigslist.org', 'sacramento.craigslist.org', 'sandiego.craigslist.org', 'sfbay.craigslist.org', 'slo.craigslist.org', 'santabarbara.craigslist.org', 'santamaria.craigslist.org', 'siskiyou.craigslist.org', 'stockton.craigslist.org', 'susanville.craigslist.org', 'ventura.craigslist.org', 'visalia.craigslist.org', 'yubasutter.craigslist.org', '', 'boulder.craigslist.org', 'cosprings.craigslist.org', 'denver.craigslist.org', 'eastco.craigslist.org', 'fortcollins.craigslist.org', 'rockies.craigslist.org', 'pueblo.craigslist.org', 'westslope.craigslist.org', '', 'newlondon.craigslist.org', 'hartford.craigslist.org', 'newhaven.craigslist.org', 'nwct.craigslist.org', '', 'delaware.craigslist.org', '', 'washingtondc.craigslist.org', '', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fbrw', 'daytona.craigslist.org', 'keys.craigslist.org', 'fortlauderdale.craigslist.org', 'fortmyers.craigslist.org', 'gainesville.craigslist.org', 'cfl.craigslist.org', 'jacksonville.craigslist.org', 'lakeland.craigslist.org', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc', 'lakecity.craigslist.org', 'ocala.craigslist.org', 'okaloosa.craigslist.org', 'orlando.craigslist.org', 'panamacity.craigslist.org', 'pensacola.craigslist.org', 'sarasota.craigslist.org', 'miami.craigslist.org', 'spacecoast.craigslist.org', 'staugustine.craigslist.org', 'tallahassee.craigslist.org', 'tampa.craigslist.org', 'treasure.craigslist.org', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc', '', 'albanyga.craigslist.org', 'athensga.craigslist.org', 'atlanta.craigslist.org', 'augusta.craigslist.org', 'brunswick.craigslist.org', 'columbusga.craigslist.org', 'macon.craigslist.org', 'nwga.craigslist.org', 'savannah.craigslist.org', 'statesboro.craigslist.org', 'valdosta.craigslist.org', '', 'honolulu.craigslist.org', '', 'boise.craigslist.org', 'eastidaho.craigslist.org', 'lewiston.craigslist.org', 'twinfalls.craigslist.org', '', 'bn.craigslist.org', 'chambana.craigslist.org', 'chicago.craigslist.org', 'decatur.craigslist.org', 'lasalle.craigslist.org', 'mattoon.craigslist.org', 'peoria.craigslist.org', 'rockford.craigslist.org', 'carbondale.craigslist.org', 'springfieldil.craigslist.org', 'quincy.craigslist.org', '', 'bloomington.craigslist.org', 'evansville.craigslist.org', 'fortwayne.craigslist.org', 'indianapolis.craigslist.org', 'kokomo.craigslist.org', 'tippecanoe.craigslist.org', 'muncie.craigslist.org', 'richmondin.craigslist.org', 'southbend.craigslist.org', 'terrehaute.craigslist.org', '', 'ames.craigslist.org', 'cedarrapids.craigslist.org', 'desmoines.craigslist.org', 'dubuque.craigslist.org', 'fortdodge.craigslist.org', 'iowacity.craigslist.org', 'masoncity.craigslist.org', 'quadcities.craigslist.org', 'siouxcity.craigslist.org', 'ottumwa.craigslist.org', 'waterloo.craigslist.org', '', 'lawrence.craigslist.org', 'ksu.craigslist.org', 'nwks.craigslist.org', 'salina.craigslist.org', 'seks.craigslist.org', 'swks.craigslist.org', 'topeka.craigslist.org', 'wichita.craigslist.org', '', 'bgky.craigslist.org', 'eastky.craigslist.org', 'lexington.craigslist.org', 'louisville.craigslist.org', 'owensboro.craigslist.org', 'westky.craigslist.org', '', 'batonrouge.craigslist.org', 'cenla.craigslist.org', 'houma.craigslist.org', 'lafayette.craigslist.org', 'lakecharles.craigslist.org', 'monroe.craigslist.org', 'neworleans.craigslist.org', 'shreveport.craigslist.org', '', 'maine.craigslist.org', '', 'annapolis.craigslist.org', 'baltimore.craigslist.org', 'easternshore.craigslist.org', 'frederick.craigslist.org', 'smd.craigslist.org', 'westmd.craigslist.org', '', 'boston.craigslist.org', 'capecod.craigslist.org', 'southcoast.craigslist.org', 'westernmass.craigslist.org', 'worcester.craigslist.org', '', 'annarbor.craigslist.org', 'battlecreek.craigslist.org', 'centralmich.craigslist.org', 'detroit.craigslist.org', 'flint.craigslist.org', 'grandrapids.craigslist.org', 'holland.craigslist.org', 'jxn.craigslist.org', 'kalamazoo.craigslist.org', 'lansing.craigslist.org', 'monroemi.craigslist.org', 'muskegon.craigslist.org', 'nmi.craigslist.org', 'porthuron.craigslist.org', 'saginaw.craigslist.org', 'swmi.craigslist.org', 'thumb.craigslist.org', 'up.craigslist.org', '', 'bemidji.craigslist.org', 'brainerd.craigslist.org', 'duluth.craigslist.org', 'mankato.craigslist.org', 'minneapolis.craigslist.org', 'rmn.craigslist.org', 'marshall.craigslist.org', 'stcloud.craigslist.org', '', 'gulfport.craigslist.org', 'hattiesburg.craigslist.org', 'jackson.craigslist.org', 'meridian.craigslist.org', 'northmiss.craigslist.org', 'natchez.craigslist.org', '', 'columbiamo.craigslist.org', 'joplin.craigslist.org', 'kansascity.craigslist.org', 'kirksville.craigslist.org', 'loz.craigslist.org', 'semo.craigslist.org', 'springfield.craigslist.org', 'stjoseph.craigslist.org', 'stlouis.craigslist.org', '', 'billings.craigslist.org', 'bozeman.craigslist.org', 'butte.craigslist.org', 'greatfalls.craigslist.org', 'helena.craigslist.org', 'kalispell.craigslist.org', 'missoula.craigslist.org', 'montana.craigslist.org', '', 'grandisland.craigslist.org', 'lincoln.craigslist.org', 'northplatte.craigslist.org', 'omaha.craigslist.org', 'scottsbluff.craigslist.org', '', 'elko.craigslist.org', 'lasvegas.craigslist.org', 'reno.craigslist.org', '', 'nh.craigslist.org', '', 'cnj.craigslist.org', 'jerseyshore.craigslist.org', 'newjersey.craigslist.org', 'southjersey.craigslist.org', '', 'albuquerque.craigslist.org', 'clovis.craigslist.org', 'farmington.craigslist.org', 'lascruces.craigslist.org', 'roswell.craigslist.org', 'santafe.craigslist.org', '', 'albany.craigslist.org', 'binghamton.craigslist.org', 'buffalo.craigslist.org', 'catskills.craigslist.org', 'chautauqua.craigslist.org', 'elmira.craigslist.org', 'fingerlakes.craigslist.org', 'glensfalls.craigslist.org', 'hudsonvalley.craigslist.org', 'ithaca.craigslist.org', 'longisland.craigslist.org', 'newyork.craigslist.org', 'oneonta.craigslist.org', 'plattsburgh.craigslist.org', 'potsdam.craigslist.org', 'rochester.craigslist.org', 'syracuse.craigslist.org', 'twintiers.craigslist.org', 'utica.craigslist.org', 'watertown.craigslist.org', '', 'asheville.craigslist.org', 'boone.craigslist.org', 'charlotte.craigslist.org', 'eastnc.craigslist.org', 'fayetteville.craigslist.org', 'greensboro.craigslist.org', 'hickory.craigslist.org', 'onslow.craigslist.org', 'outerbanks.craigslist.org', 'raleigh.craigslist.org', 'wilmington.craigslist.org', 'winstonsalem.craigslist.org', '', 'bismarck.craigslist.org', 'fargo.craigslist.org', 'grandforks.craigslist.org', 'nd.craigslist.org', '', 'akroncanton.craigslist.org', 'ashtabula.craigslist.org', 'athensohio.craigslist.org', 'chillicothe.craigslist.org', 'cincinnati.craigslist.org', 'cleveland.craigslist.org', 'columbus.craigslist.org', 'dayton.craigslist.org', 'limaohio.craigslist.org', 'mansfield.craigslist.org', 'sandusky.craigslist.org', 'toledo.craigslist.org', 'tuscarawas.craigslist.org', 'youngstown.craigslist.org', 'zanesville.craigslist.org', '', 'lawton.craigslist.org', 'enid.craigslist.org', 'oklahomacity.craigslist.org', 'stillwater.craigslist.org', 'tulsa.craigslist.org', '', 'bend.craigslist.org', 'corvallis.craigslist.org', 'eastoregon.craigslist.org', 'eugene.craigslist.org', 'klamath.craigslist.org', 'medford.craigslist.org', 'oregoncoast.craigslist.org', 'portland.craigslist.org', 'roseburg.craigslist.org', 'salem.craigslist.org', '', 'altoona.craigslist.org', 'chambersburg.craigslist.org', 'erie.craigslist.org', 'harrisburg.craigslist.org', 'lancaster.craigslist.org', 'allentown.craigslist.org', 'meadville.craigslist.org', 'philadelphia.craigslist.org', 'pittsburgh.craigslist.org', 'poconos.craigslist.org', 'reading.craigslist.org', 'scranton.craigslist.org', 'pennstate.craigslist.org', 'williamsport.craigslist.org', 'york.craigslist.org', '', 'providence.craigslist.org', '', 'charleston.craigslist.org', 'columbia.craigslist.org', 'florencesc.craigslist.org', 'greenville.craigslist.org', 'hiltonhead.craigslist.org', 'myrtlebeach.craigslist.org', '', 'nesd.craigslist.org', 'csd.craigslist.org', 'rapidcity.craigslist.org', 'siouxfalls.craigslist.org', 'sd.craigslist.org', '', 'chattanooga.craigslist.org', 'clarksville.craigslist.org', 'cookeville.craigslist.org', 'jacksontn.craigslist.org', 'knoxville.craigslist.org', 'memphis.craigslist.org', 'nashville.craigslist.org', 'tricities.craigslist.org', '', 'abilene.craigslist.org', 'amarillo.craigslist.org', 'austin.craigslist.org', 'beaumont.craigslist.org', 'brownsville.craigslist.org', 'collegestation.craigslist.org', 'corpuschristi.craigslist.org', 'dallas.craigslist.org', 'nacogdoches.craigslist.org', 'delrio.craigslist.org', 'elpaso.craigslist.org', 'galveston.craigslist.org', 'houston.craigslist.org', 'killeen.craigslist.org', 'laredo.craigslist.org', 'lubbock.craigslist.org', 'mcallen.craigslist.org', 'odessa.craigslist.org', 'sanangelo.craigslist.org', 'sanantonio.craigslist.org', 'sanmarcos.craigslist.org', 'bigbend.craigslist.org', 'texoma.craigslist.org', 'easttexas.craigslist.org', 'victoriatx.craigslist.org', 'waco.craigslist.org', 'wichitafalls.craigslist.org', '', 'logan.craigslist.org', 'ogden.craigslist.org', 'provo.craigslist.org', 'saltlakecity.craigslist.org', 'stgeorge.craigslist.org', '', 'vermont.craigslist.org', '', 'charlottesville.craigslist.org', 'danville.craigslist.org', 'fredericksburg.craigslist.org', 'norfolk.craigslist.org', 'harrisonburg.craigslist.org', 'lynchburg.craigslist.org', 'blacksburg.craigslist.org', 'richmond.craigslist.org', 'roanoke.craigslist.org', 'swva.craigslist.org', 'winchester.craigslist.org', '', 'bellingham.craigslist.org', 'kpr.craigslist.org', 'moseslake.craigslist.org', 'olympic.craigslist.org', 'pullman.craigslist.org', 'seattle.craigslist.org', 'skagit.craigslist.org', 'spokane.craigslist.org', 'wenatchee.craigslist.org', 'yakima.craigslist.org', '', 'charlestonwv.craigslist.org', 'martinsburg.craigslist.org', 'huntington.craigslist.org', 'morgantown.craigslist.org', 'wheeling.craigslist.org', 'parkersburg.craigslist.org', 'swv.craigslist.org', 'wv.craigslist.org', '', 'appleton.craigslist.org', 'eauclaire.craigslist.org', 'greenbay.craigslist.org', 'janesville.craigslist.org', 'racine.craigslist.org', 'lacrosse.craigslist.org', 'madison.craigslist.org', 'milwaukee.craigslist.org', 'northernwi.craigslist.org', 'sheboygan.craigslist.org', 'wausau.craigslist.org', '', 'wyoming.craigslist.org', '', 'micronesia.craigslist.org', 'puertorico.craigslist.org', 'virgin.craigslist.org', 'calgary.craigslist.org', '', 'edmonton.craigslist.org', 'ftmcmurray.craigslist.org', 'lethbridge.craigslist.org', 'hat.craigslist.org', 'peace.craigslist.org', 'reddeer.craigslist.org', 'cariboo.craigslist.org', '', 'comoxvalley.craigslist.org', 'abbotsford.craigslist.org', 'kamloops.craigslist.org', 'kelowna.craigslist.org', 'kootenays.craigslist.org', 'nanaimo.craigslist.org', 'princegeorge.craigslist.org', 'skeena.craigslist.org', 'sunshine.craigslist.org', 'vancouver.craigslist.org', 'victoria.craigslist.org', 'whistler.craigslist.org', 'winnipeg.craigslist.org', '', 'newbrunswick.craigslist.org', '', 'newfoundland.craigslist.org', '', 'territories.craigslist.org', '', 'yellowknife.craigslist.org', 'halifax.craigslist.org', '', 'barrie.craigslist.org', '', 'belleville.craigslist.org', 'brantford.craigslist.org', 'chatham.craigslist.org', 'cornwall.craigslist.org', 'guelph.craigslist.org', 'hamilton.craigslist.org', 'kingston.craigslist.org', 'kitchener.craigslist.org', 'londonon.craigslist.org', 'niagara.craigslist.org', 'ottawa.craigslist.org', 'owensound.craigslist.org', 'peterborough.craigslist.org', 'sarnia.craigslist.org', 'soo.craigslist.org', 'sudbury.craigslist.org', 'thunderbay.craigslist.org', 'toronto.craigslist.org', 'windsor.craigslist.org', 'pei.craigslist.org', '', 'montreal.craigslist.org', '', 'quebec.craigslist.org', 'saguenay.craigslist.org', 'sherbrooke.craigslist.org', 'troisrivieres.craigslist.org', '', '', 'regina.craigslist.org', 'saskatoon.craigslist.org', '', 'whitehorse.craigslist.org', 'vienna.craigslist.at', '', 'brussels.craigslist.org', '', 'bulgaria.craigslist.org', '', 'zagreb.craigslist.org', '', 'prague.craigslist.cz', '', 'copenhagen.craigslist.org', '', 'helsinki.craigslist.fi', '', 'bordeaux.craigslist.org', '', 'rennes.craigslist.org', 'grenoble.craigslist.org', 'lille.craigslist.org', 'loire.craigslist.org', 'lyon.craigslist.org', 'marseilles.craigslist.org', 'montpellier.craigslist.org', 'cotedazur.craigslist.org', 'rouen.craigslist.org', 'paris.craigslist.org', 'strasbourg.craigslist.org', 'toulouse.craigslist.org', 'berlin.craigslist.de', '', 'bremen.craigslist.de', 'cologne.craigslist.de', 'dresden.craigslist.de', 'dusseldorf.craigslist.de', 'essen.craigslist.de', 'frankfurt.craigslist.de', 'hamburg.craigslist.de', 'hannover.craigslist.de', 'heidelberg.craigslist.de', 'kaiserslautern.craigslist.de', 'leipzig.craigslist.de', 'munich.craigslist.de', 'nuremberg.craigslist.de', 'stuttgart.craigslist.de', 'athens.craigslist.gr', '', 'budapest.craigslist.org', '', 'reykjavik.craigslist.org', '', 'dublin.craigslist.org', '', 'bologna.craigslist.it', '', 'florence.craigslist.it', 'genoa.craigslist.it', 'milan.craigslist.it', 'naples.craigslist.it', 'perugia.craigslist.it', 'rome.craigslist.it', 'sardinia.craigslist.it', 'sicily.craigslist.it', 'torino.craigslist.it', 'venice.craigslist.it', 'luxembourg.craigslist.org', '', 'amsterdam.craigslist.org', '', 'oslo.craigslist.org', '', 'warsaw.craigslist.pl', '', 'faro.craigslist.pt', '', 'lisbon.craigslist.pt', 'porto.craigslist.pt', 'bucharest.craigslist.org', '', 'moscow.craigslist.org', '', 'stpetersburg.craigslist.org', 'alicante.craigslist.es', '', 'baleares.craigslist.es', 'barcelona.craigslist.es', 'bilbao.craigslist.es', '', 'cadiz.craigslist.es', 'canarias.craigslist.es', 'granada.craigslist.es', 'madrid.craigslist.es', 'malaga.craigslist.es', 'sevilla.craigslist.es', 'valencia.craigslist.es', '', 'stockholm.craigslist.se', '', 'basel.craigslist.ch', 'bern.craigslist.ch', 'geneva.craigslist.ch', 'lausanne.craigslist.ch', 'zurich.craigslist.ch', '', 'istanbul.craigslist.com.tr', '', 'ukraine.craigslist.org', '', 'aberdeen.craigslist.co.uk', 'bath.craigslist.co.uk', 'belfast.craigslist.co.uk', 'birmingham.craigslist.co.uk', 'brighton.craigslist.co.uk', 'bristol.craigslist.co.uk', 'cambridge.craigslist.co.uk', 'cardiff.craigslist.co.uk', 'coventry.craigslist.co.uk', 'derby.craigslist.co.uk', 'devon.craigslist.co.uk', 'dundee.craigslist.co.uk', 'norwich.craigslist.co.uk', 'eastmids.craigslist.co.uk', 'edinburgh.craigslist.co.uk', 'essex.craigslist.co.uk', 'glasgow.craigslist.co.uk', 'hampshire.craigslist.co.uk', 'kent.craigslist.co.uk', 'leeds.craigslist.co.uk', 'liverpool.craigslist.co.uk', 'london.craigslist.co.uk', 'manchester.craigslist.co.uk', 'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk', 'oxford.craigslist.co.uk', 'sheffield.craigslist.co.uk', 'bangladesh.craigslist.org', '', 'beijing.craigslist.com.cn', '', 'chengdu.craigslist.com.cn', 'chongqing.craigslist.com.cn', 'dalian.craigslist.com.cn', 'guangzhou.craigslist.com.cn', 'hangzhou.craigslist.com.cn', 'nanjing.craigslist.com.cn', 'shanghai.craigslist.com.cn', 'shenyang.craigslist.com.cn', 'shenzhen.craigslist.com.cn', 'wuhan.craigslist.com.cn', 'xian.craigslist.com.cn', 'micronesia.craigslist.org', '', 'hongkong.craigslist.hk', '', 'ahmedabad.craigslist.co.in', '', 'bangalore.craigslist.co.in', 'bhubaneswar.craigslist.co.in', 'chandigarh.craigslist.co.in', 'chennai.craigslist.co.in', 'delhi.craigslist.co.in', 'goa.craigslist.co.in', 'hyderabad.craigslist.co.in', 'indore.craigslist.co.in', 'jaipur.craigslist.co.in', 'kerala.craigslist.co.in', 'kolkata.craigslist.co.in', 'lucknow.craigslist.co.in', 'mumbai.craigslist.co.in', 'pune.craigslist.co.in', 'surat.craigslist.co.in', 'jakarta.craigslist.org', '', 'tehran.craigslist.org', '', 'baghdad.craigslist.org', '', 'haifa.craigslist.org', '', 'jerusalem.craigslist.org', 'telaviv.craigslist.org', 'ramallah.craigslist.org', 'fukuoka.craigslist.jp', '', 'hiroshima.craigslist.jp', 'nagoya.craigslist.jp', 'okinawa.craigslist.jp', 'osaka.craigslist.jp', 'sapporo.craigslist.jp', 'sendai.craigslist.jp', 'tokyo.craigslist.jp', 'seoul.craigslist.co.kr', '', 'kuwait.craigslist.org', '', 'beirut.craigslist.org', '', 'malaysia.craigslist.org', '', 'pakistan.craigslist.org', '', 'bacolod.craigslist.com.ph', '', 'naga.craigslist.com.ph', 'cdo.craigslist.com.ph', 'cebu.craigslist.com.ph', 'davaocity.craigslist.com.ph', 'iloilo.craigslist.com.ph', 'manila.craigslist.com.ph', 'pampanga.craigslist.com.ph', 'zamboanga.craigslist.com.ph', 'singapore.craigslist.com.sg', '', 'taipei.craigslist.com.tw', '', 'bangkok.craigslist.co.th', '', 'dubai.craigslist.org', '', 'vietnam.craigslist.org', '', 'adelaide.craigslist.com.au', 'brisbane.craigslist.com.au', '', 'cairns.craigslist.com.au', 'canberra.craigslist.com.au', 'darwin.craigslist.com.au', 'goldcoast.craigslist.com.au', 'melbourne.craigslist.com.au', 'ntl.craigslist.com.au', 'perth.craigslist.com.au', 'sydney.craigslist.com.au', 'hobart.craigslist.com.au', 'wollongong.craigslist.com.au', 'auckland.craigslist.org', 'christchurch.craigslist.org', '', 'dunedin.craigslist.co.nz', 'wellington.craigslist.org', 'buenosaires.craigslist.org', 'lapaz.craigslist.org', 'belohorizonte.craigslist.org', '', 'brasilia.craigslist.org', '', 'curitiba.craigslist.org', '', 'fortaleza.craigslist.org', 'portoalegre.craigslist.org', 'recife.craigslist.org', 'rio.craigslist.org', 'salvador.craigslist.org', '', 'saopaulo.craigslist.org', 'caribbean.craigslist.org', 'santiago.craigslist.org', '', 'colombia.craigslist.org', '', 'costarica.craigslist.org', '', 'santodomingo.craigslist.org', '', 'quito.craigslist.org', '', 'elsalvador.craigslist.org', '', 'guatemala.craigslist.org', '', 'acapulco.craigslist.com.mx', '', 'bajasur.craigslist.com.mx', '', 'chihuahua.craigslist.com.mx', 'juarez.craigslist.com.mx', 'guadalajara.craigslist.com.mx', 'guanajuato.craigslist.com.mx', 'hermosillo.craigslist.com.mx', 'mazatlan.craigslist.com.mx', 'mexicocity.craigslist.com.mx', 'monterrey.craigslist.com.mx', 'oaxaca.craigslist.com.mx', 'puebla.craigslist.com.mx', 'pv.craigslist.com.mx', 'tijuana.craigslist.com.mx', 'veracruz.craigslist.com.mx', 'yucatan.craigslist.com.mx', 'managua.craigslist.org', 'panama.craigslist.org', '', 'lima.craigslist.org', '', 'puertorico.craigslist.org', '', 'montevideo.craigslist.org', '', 'caracas.craigslist.org', '', 'virgin.craigslist.org', '', 'cairo.craigslist.org', '', 'addisababa.craigslist.org', 'accra.craigslist.org', '', 'kenya.craigslist.org', '', 'casablanca.craigslist.org', '', 'capetown.craigslist.co.za', '', 'durban.craigslist.co.za', '', 'johannesburg.craigslist.co.za', '', 'pretoria.craigslist.co.za', 'tunis.craigslist.org', '', '', '', '']
# link_texts = ['US', 'ALABAMA', 'Auburn', 'Birmingham', 'Dothan', 'Florence / Muscle Shoals', 'Gadsden-Anniston', 'Huntsville / Decatur', 'Mobile', 'Montgomery', 'Tuscaloosa', 'ALASKA', 'Anchorage / Mat-Su', 'Fairbanks', 'Kenai Peninsula', 'Southeast Alaska', 'ARIZONA', 'Flagstaff / Sedona', 'Mohave County', 'Phoenix', 'Prescott', 'Show Low', 'Sierra Vista', 'Tucson', 'Yuma', 'ARKANSAS', 'Fayetteville ', 'Fort Smith', 'Jonesboro', 'Little Rock', 'Texarkana', 'CALIFORNIA', 'Bakersfield', 'Chico', 'Fresno / Madera', 'Gold Country', 'Hanford-Corcoran', 'Humboldt County', 'Imperial County', 'Inland Empire', 'Los Angeles', 'Mendocino County', 'Merced', 'Modesto', 'Monterey Bay', 'Orange County', 'Palm Springs', 'Redding', 'Sacramento', 'San Diego', 'San Francisco Bay Area', 'San Luis Obispo', 'Santa Barbara', 'Santa Maria', 'Siskiyou County', 'Stockton', 'Susanville', 'Ventura County', 'Visalia-Tulare', 'Yuba-Sutter', 'COLORADO', 'Boulder', 'Colorado Springs', 'Denver', 'Eastern CO', 'Fort Collins / North CO', 'High Rockies', 'Pueblo', 'Western Slope', 'CONNECTICUT', 'Eastern CT', 'Hartford', 'New Haven', 'Northwest Ct', 'DELAWARE', 'Delaware', 'DISTRICT OF COLUMBIA', 'Washington', 'FLORIDA', 'Broward County', 'Daytona Beach', 'Florida Keys', 'Fort Lauderdale', 'Ft Myers / Sw Florida', 'Gainesville', 'Heartland Florida', 'Jacksonville', 'Lakeland', 'Miami / Dade', 'North Central FL', 'Ocala', 'Okaloosa / Walton', 'Orlando', 'Panama City', 'Pensacola', 'Sarasota-Bradenton', 'South Florida', 'Space Coast', 'St Augustine', 'Tallahassee', 'Tampa Bay Area', 'Treasure Coast', 'Palm Beach County', 'GEORGIA', 'Albany ', 'Athens', 'Atlanta', 'Augusta', 'Brunswick', 'Columbus ', 'Macon / Warner Robins', 'Northwest GA', 'Savannah / Hinesville', 'Statesboro', 'Valdosta', 'HAWAII', 'Hawaii', 'IDAHO', 'Boise', 'East Idaho', 'Lewiston / Clarkston', 'Twin Falls', 'ILLINOIS', 'Bloomington-Normal', 'Champaign Urbana', 'Chicago', 'Decatur', 'La Salle Co', 'Mattoon-Charleston', 'Peoria', 'Rockford', 'Southern Illinois', 'Springfield ', 'Western IL', 'INDIANA', 'Bloomington', 'Evansville', 'Fort Wayne', 'Indianapolis', 'Kokomo', 'Lafayette / West Lafayette', 'Muncie / Anderson', 'Richmond ', 'South Bend / Michiana', 'Terre Haute', 'IOWA', 'Ames', 'Cedar Rapids', 'Des Moines', 'Dubuque', 'Fort Dodge', 'Iowa City', 'Mason City', 'Quad Cities', 'Sioux City', 'Southeast IA', 'Waterloo / Cedar Falls', 'KANSAS', 'Lawrence', 'Manhattan', 'Northwest KS', 'Salina', 'Southeast KS', 'Southwest KS', 'Topeka', 'Wichita', 'KENTUCKY', 'Bowling Green', 'Eastern Kentucky', 'Lexington', 'Louisville', 'Owensboro', 'Western KY', 'LOUISIANA', 'Baton Rouge', 'Central Louisiana', 'Houma', 'Lafayette', 'Lake Charles', 'Monroe', 'New Orleans', 'Shreveport', 'MAINE', 'Maine', 'MARYLAND', 'Annapolis', 'Baltimore', 'Eastern Shore', 'Frederick', 'Southern Maryland', 'Western Maryland', 'MASSACHUSETTS', 'Boston', 'Cape Cod / Islands', 'South Coast', 'Western Massachusetts', 'Worcester / Central MA', 'MICHIGAN', 'Ann Arbor', 'Battle Creek', 'Central Michigan', 'Detroit Metro', 'Flint', 'Grand Rapids', 'Holland', 'Jackson ', 'Kalamazoo', 'Lansing', 'Monroe ', 'Muskegon', 'Northern Michigan', 'Port Huron', 'Saginaw-Midland-Baycity', 'Southwest Michigan', 'The Thumb', 'Upper Peninsula', 'MINNESOTA', 'Bemidji', 'Brainerd', 'Duluth / Superior', 'Mankato', 'Minneapolis / St Paul', 'Rochester ', 'Southwest MN', 'St Cloud', 'MISSISSIPPI', 'Gulfport / Biloxi', 'Hattiesburg', 'Jackson', 'Meridian', 'North Mississippi', 'Southwest MS', 'MISSOURI', 'Columbia / Jeff City', 'Joplin', 'Kansas City', 'Kirksville', 'Lake Of The Ozarks', 'Southeast Missouri', 'Springfield', 'St Joseph', 'St Louis', 'MONTANA', 'Billings', 'Bozeman', 'Butte', 'Great Falls', 'Helena', 'Kalispell', 'Missoula', 'Eastern Montana', 'NEBRASKA', 'Grand Island', 'Lincoln', 'North Platte', 'Omaha / Council Bluffs', 'Scottsbluff / Panhandle', 'NEVADA', 'Elko', 'Las Vegas', 'Reno / Tahoe', 'NEW HAMPSHIRE', 'New Hampshire', 'NEW JERSEY', 'Central NJ', 'Jersey Shore', 'North Jersey', 'South Jersey', 'NEW MEXICO', 'Albuquerque', 'Clovis / Portales', 'Farmington', 'Las Cruces', 'Roswell / Carlsbad', 'Santa Fe / Taos', 'NEW YORK', 'Albany', 'Binghamton', 'Buffalo', 'Catskills', 'Chautauqua', 'Elmira-Corning', 'Finger Lakes', 'Glens Falls', 'Hudson Valley', 'Ithaca', 'Long Island', 'New York City', 'Oneonta', 'Plattsburgh-Adirondacks', 'Potsdam-Canton-Massena', 'Rochester', 'Syracuse', 'Twin Tiers NY/PA', 'Utica-Rome-Oneida', 'Watertown', 'NORTH CAROLINA', 'Asheville', 'Boone', 'Charlotte', 'Eastern Nc', 'Fayetteville', 'Greensboro', 'Hickory / Lenoir', 'Jacksonville ', 'Outer Banks', 'Raleigh / Durham / CH', 'Wilmington', 'Winston-Salem', 'NORTH DAKOTA', 'Bismarck', 'Fargo / Moorhead', 'Grand Forks', 'North Dakota', 'OHIO', 'Akron / Canton', 'Ashtabula', 'Athens ', 'Chillicothe', 'Cincinnati', 'Cleveland', 'Columbus', 'Dayton / Springfield', 'Lima / Findlay', 'Mansfield', 'Sandusky', 'Toledo', 'Tuscarawas Co', 'Youngstown', 'Zanesville / Cambridge', 'OKLAHOMA', 'Lawton', 'Northwest OK', 'Oklahoma City', 'Stillwater', 'Tulsa', 'OREGON', 'Bend', 'Corvallis/Albany', 'East Oregon', 'Eugene', 'Klamath Falls', 'Medford-Ashland', 'Oregon Coast', 'Portland', 'Roseburg', 'Salem', 'PENNSYLVANIA', 'Altoona-Johnstown', 'Cumberland Valley', 'Erie', 'Harrisburg', 'Lancaster', 'Lehigh Valley', 'Meadville', 'Philadelphia', 'Pittsburgh', 'Poconos', 'Reading', 'Scranton / Wilkes-Barre', 'State College', 'Williamsport', 'York', 'RHODE ISLAND', 'Rhode Island', 'SOUTH CAROLINA', 'Charleston', 'Columbia', 'Florence', 'Greenville / Upstate', 'Hilton Head', 'Myrtle Beach', 'SOUTH DAKOTA', 'Northeast SD', 'Pierre / Central SD', 'Rapid City / West SD', 'Sioux Falls / Se SD', 'South Dakota', 'TENNESSEE', 'Chattanooga', 'Clarksville', 'Cookeville', 'Jackson  ', 'Knoxville', 'Memphis', 'Nashville', 'Tri-Cities', 'TEXAS', 'Abilene', 'Amarillo', 'Austin', 'Beaumont / Port Arthur', 'Brownsville', 'College Station', 'Corpus Christi', 'Dallas / Fort Worth', 'Deep East Texas', 'Del Rio / Eagle Pass', 'El Paso', 'Galveston', 'Houston', 'Killeen / Temple / Ft Hood', 'Laredo', 'Lubbock', 'Mcallen / Edinburg', 'Odessa / Midland', 'San Angelo', 'San Antonio', 'San Marcos', 'Southwest TX', 'Texoma', 'Tyler / East TX', 'Victoria ', 'Waco', 'Wichita Falls', 'UTAH', 'Logan', 'Ogden-Clearfield', 'Provo / Orem', 'Salt Lake City', 'St George', 'VERMONT', 'Vermont', 'VIRGINIA', 'Charlottesville', 'Danville', 'Fredericksburg', 'Hampton Roads', 'Harrisonburg', 'Lynchburg', 'New River Valley', 'Richmond', 'Roanoke', 'Southwest VA', 'Winchester', 'WASHINGTON', 'Bellingham', 'Kennewick-Pasco-Richland', 'Moses Lake', 'Olympic Peninsula', 'Pullman / Moscow', 'Seattle-Tacoma', 'Skagit / Island / SJI', "Spokane / Coeur D'Alene", 'Wenatchee', 'Yakima', 'WEST VIRGINIA', 'Charleston ', 'Eastern Panhandle', 'Huntington-Ashland', 'Morgantown', 'Northern Panhandle', 'Parkersburg-Marietta', 'Southern WV', 'West Virginia (Old)', 'WISCONSIN', 'Appleton-Oshkosh-FDL', 'Eau Claire', 'Green Bay', 'Janesville', 'Kenosha-Racine', 'La Crosse', 'Madison', 'Milwaukee', 'Northern Wi', 'Sheboygan', 'Wausau', 'WYOMING', 'Wyoming', 'TERRITORIES', 'Guam-Micronesia', 'Puerto Rico', 'U.S. Virgin Islands', 'CANADA', 'ALBERTA', 'Calgary', 'Edmonton', 'Ft Mcmurray', 'Lethbridge', 'Medicine Hat', 'Peace River Country', 'Red Deer', 'BRITISH COLUMBIA', 'Cariboo', 'Comox Valley', 'Fraser Valley', 'Kamloops', 'Kelowna / Okanagan', 'Kootenays', 'Nanaimo', 'Prince George', 'Skeena-Bulkley', 'Sunshine Coast', 'Vancouver', 'Victoria', 'Whistler', 'MANITOBA', 'Winnipeg', 'NEW BRUNSWICK', 'New Brunswick', 'NEWFOUNDLAND AND LABRADOR', "St John'S", 'NORTHWEST TERRITORIES', 'Territories', 'Yellowknife', 'NOVA SCOTIA', 'Halifax', 'ONTARIO', 'Barrie', 'Belleville', 'Brantford-Woodstock', 'Chatham-Kent', 'Cornwall', 'Guelph', 'Hamilton-Burlington', 'Kingston', 'Kitchener-Waterloo-Cambridge', 'London ', 'Niagara Region', 'Ottawa-Hull-Gatineau', 'Owen Sound', 'Peterborough', 'Sarnia', 'Sault Ste Marie', 'Sudbury', 'Thunder Bay', 'Toronto', 'Windsor', 'PRINCE EDWARD ISLAND', 'Prince Edward Island', 'QUEBEC', 'Montreal', 'Quebec City', 'Saguenay', 'Sherbrooke', 'Trois-Rivieres', 'SASKATCHEWAN', 'Regina', 'Saskatoon', 'YUKON TERRITORY', 'Whitehorse', 'EUROPE', 'AUSTRIA', 'Vienna', 'BELGIUM', 'Belgium', 'BULGARIA', 'Bulgaria', 'CROATIA', 'Croatia', 'CZECH REPUBLIC', 'Prague', 'DENMARK', 'Copenhagen', 'FINLAND', 'Finland', 'FRANCE', 'Bordeaux', 'Brittany', 'Grenoble', 'Lille', 'Loire Valley', 'Lyon', 'Marseille', 'Montpellier', "Nice / Cote D'Azur", 'Normandy', 'Paris', 'Strasbourg', 'Toulouse', 'GERMANY', 'Berlin', 'Bremen', 'Cologne', 'Dresden', 'Dusseldorf', 'Essen / Ruhr', 'Frankfurt', 'Hamburg', 'Hannover', 'Heidelberg', 'Kaiserslautern', 'Leipzig', 'Munich', 'Nuremberg', 'Stuttgart', 'GREECE', 'Greece', 'HUNGARY', 'Budapest', 'ICELAND', 'Reykjavik', 'IRELAND', 'Dublin', 'ITALY', 'Bologna', 'Florence / Tuscany', 'Genoa', 'Milan', 'Napoli / Campania', 'Perugia', 'Rome', 'Sardinia', 'Sicilia', 'Torino', 'Venice / Veneto', 'LUXEMBOURG', 'Luxembourg', 'NETHERLANDS', 'Amsterdam / Randstad', 'NORWAY', 'Norway', 'POLAND', 'Poland', 'PORTUGAL', 'Faro / Algarve', 'Lisbon', 'Porto', 'ROMANIA', 'Romania', 'RUSSIAN FEDERATION', 'Moscow', 'St Petersburg', 'SPAIN', 'Alicante', 'Baleares', 'Barcelona', 'Bilbao', 'Cadiz', 'Canarias', 'Granada', 'Madrid', 'Malaga', 'Sevilla', 'Valencia', 'SWEDEN', 'Sweden', 'SWITZERLAND', 'Basel', 'Bern', 'Geneva', 'Lausanne', 'Zurich', 'TURKEY', 'Turkey', 'UKRAINE', 'Ukraine', 'UNITED KINGDOM', 'Aberdeen', 'Bath', 'Belfast', 'Birmingham / West Mids', 'Brighton', 'Bristol', 'Cambridge, UK', 'Cardiff / Wales', 'Coventry', 'Derby', 'Devon & Cornwall', 'Dundee', 'East Anglia', 'East Midlands', 'Edinburgh', 'Essex', 'Glasgow', 'Hampshire', 'Kent', 'Leeds', 'Liverpool', 'London', 'Manchester', 'Newcastle / NE England', 'Nottingham', 'Oxford', 'Sheffield', 'ASIA, PACIFIC AND MIDDLE EAST', 'BANGLADESH', 'Bangladesh', 'CHINA', 'Beijing', 'Chengdu', 'Chongqing', 'Dalian', 'Guangzhou', 'Hangzhou', 'Nanjing', 'Shanghai', 'Shenyang', 'Shenzhen', 'Wuhan', "Xi'An", 'GUAM / MICRONESIA', 'Guam-Micronesia', 'HONG KONG', 'Hong Kong', 'INDIA', 'Ahmedabad', 'Bangalore', 'Bhubaneswar', 'Chandigarh', 'Chennai (Madras)', 'Delhi', 'Goa', 'Hyderabad', 'Indore', 'Jaipur', 'Kerala', 'Kolkata (Calcutta)', 'Lucknow', 'Mumbai', 'Pune', 'Surat Surat', 'INDONESIA', 'Indonesia', 'IRAN', 'Iran', 'IRAQ', 'Iraq', 'ISRAEL AND PALESTINE', 'Haifa', 'Jerusalem', 'Tel Aviv', 'West Bank', 'JAPAN', 'Fukuoka', 'Hiroshima', 'Nagoya', 'Okinawa', 'Osaka-Kobe-Kyoto', 'Sapporo', 'Sendai', 'Tokyo', 'KOREA', 'Seoul', 'KUWAIT', 'Kuwait', 'LEBANON', 'Beirut, Lebanon', 'MALAYSIA', 'Malaysia', 'PAKISTAN', 'Pakistan', 'PHILIPPINES', 'Bacolod', 'Bicol Region', 'Cagayan De Oro', 'Cebu', 'Davao City', 'Iloilo', 'Manila', 'Pampanga', 'Zamboanga', 'SINGAPORE', 'Singapore', 'TAIWAN', 'Taiwan', 'THAILAND', 'Thailand', 'UNITED ARAB EMIRATES', 'United Arab Emirates', 'VIETNAM', 'Vietnam', 'OCEANIA', 'AUSTRALIA', 'Adelaide', 'Brisbane', 'Cairns', 'Canberra', 'Darwin', 'Gold Coast', 'Melbourne', 'Newcastle, NSW', 'Perth', 'Sydney', 'Tasmania', 'Wollongong', 'NEW ZEALAND', 'Auckland', 'Christchurch', 'Dunedin', 'Wellington', 'LATIN AMERICA AND CARIBBEAN', 'ARGENTINA', 'Buenos Aires', 'BOLIVIA', 'Bolivia', 'BRAZIL', 'Belo Horizonte', 'Brasilia', 'Curitiba', 'Fortaleza', 'Porto Alegre', 'Recife', 'Rio De Janeiro', 'Salvador, Bahia', 'Sao Paulo', 'CARIBBEAN ISLANDS', 'Caribbean Islands', 'CHILE', 'Chile', 'COLOMBIA', 'Colombia', 'COSTA RICA', 'Costa Rica', 'DOMINICAN REPUBLIC', 'Dominican Republic', 'ECUADOR', 'Ecuador', 'EL SALVADOR', 'El Salvador', 'GUATEMALA', 'Guatemala', 'MEXICO', 'Acapulco', 'Baja California Sur', 'Chihuahua', 'Ciudad Juarez', 'Guadalajara', 'Guanajuato', 'Hermosillo', 'Mazatlan', 'Mexico City', 'Monterrey', 'Oaxaca', 'Puebla', 'Puerto Vallarta', 'Tijuana', 'Veracruz', 'Yucatan', 'NICARAGUA', 'Nicaragua', 'PANAMA', 'Panama', 'PERU', 'Peru', 'PUERTO RICO', 'Puerto Rico', 'URUGUAY', 'Montevideo', 'VENEZUELA', 'Venezuela', 'VIRGIN ISLANDS, U.S.', 'Virgin Islands', 'AFRICA', 'EGYPT', 'Egypt', 'ETHIOPIA', 'Ethiopia', 'GHANA', 'Ghana', 'KENYA', 'Kenya', 'MOROCCO', 'Morocco', 'SOUTH AFRICA', 'Cape Town', 'Durban', 'Johannesburg', 'Pretoria', 'TUNISIA', 'Tunisia']

# ml = [links, link_texts]
# for iteration in range(861):
#     if links[iteration] == '':
#         if link_texts[iteration].isupper():
#             print('EMPTY LINK; DISABLED LINK TEXT')
#     else:
#         print(links[iteration], ': ', link_texts[iteration])

# /go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc :  Miami / Dade
# /go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc :  Palm Beach County
# links = ['auburn.craigslist.org', 'bham.craigslist.org', 'dothan.craigslist.org', 'shoals.craigslist.org',
#          'gadsden.craigslist.org', 'huntsville.craigslist.org', 'mobile.craigslist.org', 'montgomery.craigslist.org',
#          'tuscaloosa.craigslist.org', 'anchorage.craigslist.org', 'fairbanks.craigslist.org', 'kenai.craigslist.org',
#          'juneau.craigslist.org', 'flagstaff.craigslist.org', 'mohave.craigslist.org', 'phoenix.craigslist.org',
#          'prescott.craigslist.org', 'showlow.craigslist.org', 'sierravista.craigslist.org', 'tucson.craigslist.org',
#          'yuma.craigslist.org', 'fayar.craigslist.org', 'fortsmith.craigslist.org', 'jonesboro.craigslist.org',
#          'littlerock.craigslist.org', 'texarkana.craigslist.org', 'bakersfield.craigslist.org', 'chico.craigslist.org',
#          'fresno.craigslist.org', 'goldcountry.craigslist.org', 'hanford.craigslist.org', 'humboldt.craigslist.org',
#          'imperial.craigslist.org', 'inlandempire.craigslist.org', 'losangeles.craigslist.org',
#          'mendocino.craigslist.org', 'merced.craigslist.org', 'modesto.craigslist.org', 'monterey.craigslist.org',
#          'orangecounty.craigslist.org', 'palmsprings.craigslist.org', 'redding.craigslist.org',
#          'sacramento.craigslist.org', 'sandiego.craigslist.org', 'sfbay.craigslist.org', 'slo.craigslist.org',
#          'santabarbara.craigslist.org', 'santamaria.craigslist.org', 'siskiyou.craigslist.org',
#          'stockton.craigslist.org', 'susanville.craigslist.org', 'ventura.craigslist.org', 'visalia.craigslist.org',
#          'yubasutter.craigslist.org', 'boulder.craigslist.org', 'cosprings.craigslist.org', 'denver.craigslist.org',
#          'eastco.craigslist.org', 'fortcollins.craigslist.org', 'rockies.craigslist.org', 'pueblo.craigslist.org',
#          'westslope.craigslist.org', 'newlondon.craigslist.org', 'hartford.craigslist.org', 'newhaven.craigslist.org',
#          'nwct.craigslist.org', 'delaware.craigslist.org', 'washingtondc.craigslist.org',
#          '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fbrw', 'daytona.craigslist.org', 'keys.craigslist.org',
#          'fortlauderdale.craigslist.org', 'fortmyers.craigslist.org', 'gainesville.craigslist.org',
#          'cfl.craigslist.org', 'jacksonville.craigslist.org', 'lakeland.craigslist.org',
#          '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc', 'lakecity.craigslist.org', 'ocala.craigslist.org',
#          'okaloosa.craigslist.org', 'orlando.craigslist.org', 'panamacity.craigslist.org', 'pensacola.craigslist.org',
#          'sarasota.craigslist.org', 'miami.craigslist.org', 'spacecoast.craigslist.org', 'staugustine.craigslist.org',
#          'tallahassee.craigslist.org', 'tampa.craigslist.org', 'treasure.craigslist.org',
#          '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc', 'albanyga.craigslist.org', 'athensga.craigslist.org',
#          'atlanta.craigslist.org', 'augusta.craigslist.org', 'brunswick.craigslist.org', 'columbusga.craigslist.org',
#          'macon.craigslist.org', 'nwga.craigslist.org', 'savannah.craigslist.org', 'statesboro.craigslist.org',
#          'valdosta.craigslist.org', 'honolulu.craigslist.org', 'boise.craigslist.org', 'eastidaho.craigslist.org',
#          'lewiston.craigslist.org', 'twinfalls.craigslist.org', 'bn.craigslist.org', 'chambana.craigslist.org',
#          'chicago.craigslist.org', 'decatur.craigslist.org', 'lasalle.craigslist.org', 'mattoon.craigslist.org',
#          'peoria.craigslist.org', 'rockford.craigslist.org', 'carbondale.craigslist.org',
#          'springfieldil.craigslist.org', 'quincy.craigslist.org', 'bloomington.craigslist.org',
#          'evansville.craigslist.org', 'fortwayne.craigslist.org', 'indianapolis.craigslist.org',
#          'kokomo.craigslist.org', 'tippecanoe.craigslist.org', 'muncie.craigslist.org', 'richmondin.craigslist.org',
#          'southbend.craigslist.org', 'terrehaute.craigslist.org', 'ames.craigslist.org', 'cedarrapids.craigslist.org',
#          'desmoines.craigslist.org', 'dubuque.craigslist.org', 'fortdodge.craigslist.org', 'iowacity.craigslist.org',
#          'masoncity.craigslist.org', 'quadcities.craigslist.org', 'siouxcity.craigslist.org', 'ottumwa.craigslist.org',
#          'waterloo.craigslist.org', 'lawrence.craigslist.org', 'ksu.craigslist.org', 'nwks.craigslist.org',
#          'salina.craigslist.org', 'seks.craigslist.org', 'swks.craigslist.org', 'topeka.craigslist.org',
#          'wichita.craigslist.org', 'bgky.craigslist.org', 'eastky.craigslist.org', 'lexington.craigslist.org',
#          'louisville.craigslist.org', 'owensboro.craigslist.org', 'westky.craigslist.org', 'batonrouge.craigslist.org',
#          'cenla.craigslist.org', 'houma.craigslist.org', 'lafayette.craigslist.org', 'lakecharles.craigslist.org',
#          'monroe.craigslist.org', 'neworleans.craigslist.org', 'shreveport.craigslist.org', 'maine.craigslist.org',
#          'annapolis.craigslist.org', 'baltimore.craigslist.org', 'easternshore.craigslist.org',
#          'frederick.craigslist.org', 'smd.craigslist.org', 'westmd.craigslist.org', 'boston.craigslist.org',
#          'capecod.craigslist.org', 'southcoast.craigslist.org', 'westernmass.craigslist.org',
#          'worcester.craigslist.org', 'annarbor.craigslist.org', 'battlecreek.craigslist.org',
#          'centralmich.craigslist.org', 'detroit.craigslist.org', 'flint.craigslist.org', 'grandrapids.craigslist.org',
#          'holland.craigslist.org', 'jxn.craigslist.org', 'kalamazoo.craigslist.org', 'lansing.craigslist.org',
#          'monroemi.craigslist.org', 'muskegon.craigslist.org', 'nmi.craigslist.org', 'porthuron.craigslist.org',
#          'saginaw.craigslist.org', 'swmi.craigslist.org', 'thumb.craigslist.org', 'up.craigslist.org',
#          'bemidji.craigslist.org', 'brainerd.craigslist.org', 'duluth.craigslist.org', 'mankato.craigslist.org',
#          'minneapolis.craigslist.org', 'rmn.craigslist.org', 'marshall.craigslist.org', 'stcloud.craigslist.org',
#          'gulfport.craigslist.org', 'hattiesburg.craigslist.org', 'jackson.craigslist.org', 'meridian.craigslist.org',
#          'northmiss.craigslist.org', 'natchez.craigslist.org', 'columbiamo.craigslist.org', 'joplin.craigslist.org',
#          'kansascity.craigslist.org', 'kirksville.craigslist.org', 'loz.craigslist.org', 'semo.craigslist.org',
#          'springfield.craigslist.org', 'stjoseph.craigslist.org', 'stlouis.craigslist.org', 'billings.craigslist.org',
#          'bozeman.craigslist.org', 'butte.craigslist.org', 'greatfalls.craigslist.org', 'helena.craigslist.org',
#          'kalispell.craigslist.org', 'missoula.craigslist.org', 'montana.craigslist.org', 'grandisland.craigslist.org',
#          'lincoln.craigslist.org', 'northplatte.craigslist.org', 'omaha.craigslist.org', 'scottsbluff.craigslist.org',
#          'elko.craigslist.org', 'lasvegas.craigslist.org', 'reno.craigslist.org', 'nh.craigslist.org',
#          'cnj.craigslist.org', 'jerseyshore.craigslist.org', 'newjersey.craigslist.org', 'southjersey.craigslist.org',
#          'albuquerque.craigslist.org', 'clovis.craigslist.org', 'farmington.craigslist.org', 'lascruces.craigslist.org',
#          'roswell.craigslist.org', 'santafe.craigslist.org', 'albany.craigslist.org', 'binghamton.craigslist.org',
#          'buffalo.craigslist.org', 'catskills.craigslist.org', 'chautauqua.craigslist.org', 'elmira.craigslist.org',
#          'fingerlakes.craigslist.org', 'glensfalls.craigslist.org', 'hudsonvalley.craigslist.org',
#          'ithaca.craigslist.org', 'longisland.craigslist.org', 'newyork.craigslist.org', 'oneonta.craigslist.org',
#          'plattsburgh.craigslist.org', 'potsdam.craigslist.org', 'rochester.craigslist.org', 'syracuse.craigslist.org',
#          'twintiers.craigslist.org', 'utica.craigslist.org', 'watertown.craigslist.org', 'asheville.craigslist.org',
#          'boone.craigslist.org', 'charlotte.craigslist.org', 'eastnc.craigslist.org', 'fayetteville.craigslist.org',
#          'greensboro.craigslist.org', 'hickory.craigslist.org', 'onslow.craigslist.org', 'outerbanks.craigslist.org',
#          'raleigh.craigslist.org', 'wilmington.craigslist.org', 'winstonsalem.craigslist.org',
#          'bismarck.craigslist.org', 'fargo.craigslist.org', 'grandforks.craigslist.org', 'nd.craigslist.org',
#          'akroncanton.craigslist.org', 'ashtabula.craigslist.org', 'athensohio.craigslist.org',
#          'chillicothe.craigslist.org', 'cincinnati.craigslist.org', 'cleveland.craigslist.org',
#          'columbus.craigslist.org', 'dayton.craigslist.org', 'limaohio.craigslist.org', 'mansfield.craigslist.org',
#          'sandusky.craigslist.org', 'toledo.craigslist.org', 'tuscarawas.craigslist.org', 'youngstown.craigslist.org',
#          'zanesville.craigslist.org', 'lawton.craigslist.org', 'enid.craigslist.org', 'oklahomacity.craigslist.org',
#          'stillwater.craigslist.org', 'tulsa.craigslist.org', 'bend.craigslist.org', 'corvallis.craigslist.org',
#          'eastoregon.craigslist.org', 'eugene.craigslist.org', 'klamath.craigslist.org', 'medford.craigslist.org',
#          'oregoncoast.craigslist.org', 'portland.craigslist.org', 'roseburg.craigslist.org', 'salem.craigslist.org',
#          'altoona.craigslist.org', 'chambersburg.craigslist.org', 'erie.craigslist.org', 'harrisburg.craigslist.org',
#          'lancaster.craigslist.org', 'allentown.craigslist.org', 'meadville.craigslist.org',
#          'philadelphia.craigslist.org', 'pittsburgh.craigslist.org', 'poconos.craigslist.org', 'reading.craigslist.org',
#          'scranton.craigslist.org', 'pennstate.craigslist.org', 'williamsport.craigslist.org', 'york.craigslist.org',
#          'providence.craigslist.org', 'charleston.craigslist.org', 'columbia.craigslist.org',
#          'florencesc.craigslist.org', 'greenville.craigslist.org', 'hiltonhead.craigslist.org',
#          'myrtlebeach.craigslist.org', 'nesd.craigslist.org', 'csd.craigslist.org', 'rapidcity.craigslist.org',
#          'siouxfalls.craigslist.org', 'sd.craigslist.org', 'chattanooga.craigslist.org', 'clarksville.craigslist.org',
#          'cookeville.craigslist.org', 'jacksontn.craigslist.org', 'knoxville.craigslist.org', 'memphis.craigslist.org',
#          'nashville.craigslist.org', 'tricities.craigslist.org', 'abilene.craigslist.org', 'amarillo.craigslist.org',
#          'austin.craigslist.org', 'beaumont.craigslist.org', 'brownsville.craigslist.org',
#          'collegestation.craigslist.org', 'corpuschristi.craigslist.org', 'dallas.craigslist.org',
#          'nacogdoches.craigslist.org', 'delrio.craigslist.org', 'elpaso.craigslist.org', 'galveston.craigslist.org',
#          'houston.craigslist.org', 'killeen.craigslist.org', 'laredo.craigslist.org', 'lubbock.craigslist.org',
#          'mcallen.craigslist.org', 'odessa.craigslist.org', 'sanangelo.craigslist.org', 'sanantonio.craigslist.org',
#          'sanmarcos.craigslist.org', 'bigbend.craigslist.org', 'texoma.craigslist.org', 'easttexas.craigslist.org',
#          'victoriatx.craigslist.org', 'waco.craigslist.org', 'wichitafalls.craigslist.org', 'logan.craigslist.org',
#          'ogden.craigslist.org', 'provo.craigslist.org', 'saltlakecity.craigslist.org', 'stgeorge.craigslist.org',
#          'vermont.craigslist.org', 'charlottesville.craigslist.org', 'danville.craigslist.org',
#          'fredericksburg.craigslist.org', 'norfolk.craigslist.org', 'harrisonburg.craigslist.org',
#          'lynchburg.craigslist.org', 'blacksburg.craigslist.org', 'richmond.craigslist.org', 'roanoke.craigslist.org',
#          'swva.craigslist.org', 'winchester.craigslist.org', 'bellingham.craigslist.org', 'kpr.craigslist.org',
#          'moseslake.craigslist.org', 'olympic.craigslist.org', 'pullman.craigslist.org', 'seattle.craigslist.org',
#          'skagit.craigslist.org', 'spokane.craigslist.org', 'wenatchee.craigslist.org', 'yakima.craigslist.org',
#          'charlestonwv.craigslist.org', 'martinsburg.craigslist.org', 'huntington.craigslist.org',
#          'morgantown.craigslist.org', 'wheeling.craigslist.org', 'parkersburg.craigslist.org', 'swv.craigslist.org',
#          'wv.craigslist.org', 'appleton.craigslist.org', 'eauclaire.craigslist.org', 'greenbay.craigslist.org',
#          'janesville.craigslist.org', 'racine.craigslist.org', 'lacrosse.craigslist.org', 'madison.craigslist.org',
#          'milwaukee.craigslist.org', 'northernwi.craigslist.org', 'sheboygan.craigslist.org', 'wausau.craigslist.org',
#          'wyoming.craigslist.org', 'micronesia.craigslist.org', 'puertorico.craigslist.org', 'virgin.craigslist.org',
#          'calgary.craigslist.org', 'edmonton.craigslist.org', 'ftmcmurray.craigslist.org', 'lethbridge.craigslist.org',
#          'hat.craigslist.org', 'peace.craigslist.org', 'reddeer.craigslist.org', 'cariboo.craigslist.org',
#          'comoxvalley.craigslist.org', 'abbotsford.craigslist.org', 'kamloops.craigslist.org', 'kelowna.craigslist.org',
#          'kootenays.craigslist.org', 'nanaimo.craigslist.org', 'princegeorge.craigslist.org', 'skeena.craigslist.org',
#          'sunshine.craigslist.org', 'vancouver.craigslist.org', 'victoria.craigslist.org', 'whistler.craigslist.org',
#          'winnipeg.craigslist.org', 'newbrunswick.craigslist.org', 'newfoundland.craigslist.org',
#          'territories.craigslist.org', 'yellowknife.craigslist.org', 'halifax.craigslist.org', 'barrie.craigslist.org',
#          'belleville.craigslist.org', 'brantford.craigslist.org', 'chatham.craigslist.org', 'cornwall.craigslist.org',
#          'guelph.craigslist.org', 'hamilton.craigslist.org', 'kingston.craigslist.org', 'kitchener.craigslist.org',
#          'londonon.craigslist.org', 'niagara.craigslist.org', 'ottawa.craigslist.org', 'owensound.craigslist.org',
#          'peterborough.craigslist.org', 'sarnia.craigslist.org', 'soo.craigslist.org', 'sudbury.craigslist.org',
#          'thunderbay.craigslist.org', 'toronto.craigslist.org', 'windsor.craigslist.org', 'pei.craigslist.org',
#          'montreal.craigslist.org', 'quebec.craigslist.org', 'saguenay.craigslist.org', 'sherbrooke.craigslist.org',
#          'troisrivieres.craigslist.org', 'regina.craigslist.org', 'saskatoon.craigslist.org',
#          'whitehorse.craigslist.org', 'vienna.craigslist.at', 'brussels.craigslist.org', 'bulgaria.craigslist.org',
#          'zagreb.craigslist.org', 'prague.craigslist.cz', 'copenhagen.craigslist.org', 'helsinki.craigslist.fi',
#          'bordeaux.craigslist.org', 'rennes.craigslist.org', 'grenoble.craigslist.org', 'lille.craigslist.org',
#          'loire.craigslist.org', 'lyon.craigslist.org', 'marseilles.craigslist.org', 'montpellier.craigslist.org',
#          'cotedazur.craigslist.org', 'rouen.craigslist.org', 'paris.craigslist.org', 'strasbourg.craigslist.org',
#          'toulouse.craigslist.org', 'berlin.craigslist.de', 'bremen.craigslist.de', 'cologne.craigslist.de',
#          'dresden.craigslist.de', 'dusseldorf.craigslist.de', 'essen.craigslist.de', 'frankfurt.craigslist.de',
#          'hamburg.craigslist.de', 'hannover.craigslist.de', 'heidelberg.craigslist.de', 'kaiserslautern.craigslist.de',
#          'leipzig.craigslist.de', 'munich.craigslist.de', 'nuremberg.craigslist.de', 'stuttgart.craigslist.de',
#          'athens.craigslist.gr', 'budapest.craigslist.org', 'reykjavik.craigslist.org', 'dublin.craigslist.org',
#          'bologna.craigslist.it', 'florence.craigslist.it', 'genoa.craigslist.it', 'milan.craigslist.it',
#          'naples.craigslist.it', 'perugia.craigslist.it', 'rome.craigslist.it', 'sardinia.craigslist.it',
#          'sicily.craigslist.it', 'torino.craigslist.it', 'venice.craigslist.it', 'luxembourg.craigslist.org',
#          'amsterdam.craigslist.org', 'oslo.craigslist.org', 'warsaw.craigslist.pl', 'faro.craigslist.pt',
#          'lisbon.craigslist.pt', 'porto.craigslist.pt', 'bucharest.craigslist.org', 'moscow.craigslist.org',
#          'stpetersburg.craigslist.org', 'alicante.craigslist.es', 'baleares.craigslist.es', 'barcelona.craigslist.es',
#          'bilbao.craigslist.es', 'cadiz.craigslist.es', 'canarias.craigslist.es', 'granada.craigslist.es',
#          'madrid.craigslist.es', 'malaga.craigslist.es', 'sevilla.craigslist.es', 'valencia.craigslist.es',
#          'stockholm.craigslist.se', 'basel.craigslist.ch', 'bern.craigslist.ch', 'geneva.craigslist.ch',
#          'lausanne.craigslist.ch', 'zurich.craigslist.ch', 'istanbul.craigslist.com.tr', 'ukraine.craigslist.org',
#          'aberdeen.craigslist.co.uk', 'bath.craigslist.co.uk', 'belfast.craigslist.co.uk',
#          'birmingham.craigslist.co.uk', 'brighton.craigslist.co.uk', 'bristol.craigslist.co.uk',
#          'cambridge.craigslist.co.uk', 'cardiff.craigslist.co.uk', 'coventry.craigslist.co.uk',
#          'derby.craigslist.co.uk', 'devon.craigslist.co.uk', 'dundee.craigslist.co.uk', 'norwich.craigslist.co.uk',
#          'eastmids.craigslist.co.uk', 'edinburgh.craigslist.co.uk', 'essex.craigslist.co.uk',
#          'glasgow.craigslist.co.uk', 'hampshire.craigslist.co.uk', 'kent.craigslist.co.uk', 'leeds.craigslist.co.uk',
#          'liverpool.craigslist.co.uk', 'london.craigslist.co.uk', 'manchester.craigslist.co.uk',
#          'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk', 'oxford.craigslist.co.uk',
#          'sheffield.craigslist.co.uk', 'bangladesh.craigslist.org', 'beijing.craigslist.com.cn',
#          'chengdu.craigslist.com.cn', 'chongqing.craigslist.com.cn', 'dalian.craigslist.com.cn',
#          'guangzhou.craigslist.com.cn', 'hangzhou.craigslist.com.cn', 'nanjing.craigslist.com.cn',
#          'shanghai.craigslist.com.cn', 'shenyang.craigslist.com.cn', 'shenzhen.craigslist.com.cn',
#          'wuhan.craigslist.com.cn', 'xian.craigslist.com.cn', 'micronesia.craigslist.org', 'hongkong.craigslist.hk',
#          'ahmedabad.craigslist.co.in', 'bangalore.craigslist.co.in', 'bhubaneswar.craigslist.co.in',
#          'chandigarh.craigslist.co.in', 'chennai.craigslist.co.in', 'delhi.craigslist.co.in', 'goa.craigslist.co.in',
#          'hyderabad.craigslist.co.in', 'indore.craigslist.co.in', 'jaipur.craigslist.co.in', 'kerala.craigslist.co.in',
#          'kolkata.craigslist.co.in', 'lucknow.craigslist.co.in', 'mumbai.craigslist.co.in', 'pune.craigslist.co.in',
#          'surat.craigslist.co.in', 'jakarta.craigslist.org', 'tehran.craigslist.org', 'baghdad.craigslist.org',
#          'haifa.craigslist.org', 'jerusalem.craigslist.org', 'telaviv.craigslist.org', 'ramallah.craigslist.org',
#          'fukuoka.craigslist.jp', 'hiroshima.craigslist.jp', 'nagoya.craigslist.jp', 'okinawa.craigslist.jp',
#          'osaka.craigslist.jp', 'sapporo.craigslist.jp', 'sendai.craigslist.jp', 'tokyo.craigslist.jp',
#          'seoul.craigslist.co.kr', 'kuwait.craigslist.org', 'beirut.craigslist.org', 'malaysia.craigslist.org',
#          'pakistan.craigslist.org', 'bacolod.craigslist.com.ph', 'naga.craigslist.com.ph', 'cdo.craigslist.com.ph',
#          'cebu.craigslist.com.ph', 'davaocity.craigslist.com.ph', 'iloilo.craigslist.com.ph',
#          'manila.craigslist.com.ph', 'pampanga.craigslist.com.ph', 'zamboanga.craigslist.com.ph',
#          'singapore.craigslist.com.sg', 'taipei.craigslist.com.tw', 'bangkok.craigslist.co.th', 'dubai.craigslist.org',
#          'vietnam.craigslist.org', 'adelaide.craigslist.com.au', 'brisbane.craigslist.com.au',
#          'cairns.craigslist.com.au', 'canberra.craigslist.com.au', 'darwin.craigslist.com.au',
#          'goldcoast.craigslist.com.au', 'melbourne.craigslist.com.au', 'ntl.craigslist.com.au',
#          'perth.craigslist.com.au', 'sydney.craigslist.com.au', 'hobart.craigslist.com.au',
#          'wollongong.craigslist.com.au', 'auckland.craigslist.org', 'christchurch.craigslist.org',
#          'dunedin.craigslist.co.nz', 'wellington.craigslist.org', 'buenosaires.craigslist.org', 'lapaz.craigslist.org',
#          'belohorizonte.craigslist.org', 'brasilia.craigslist.org', 'curitiba.craigslist.org',
#          'fortaleza.craigslist.org', 'portoalegre.craigslist.org', 'recife.craigslist.org', 'rio.craigslist.org',
#          'salvador.craigslist.org', 'saopaulo.craigslist.org', 'caribbean.craigslist.org', 'santiago.craigslist.org',
#          'colombia.craigslist.org', 'costarica.craigslist.org', 'santodomingo.craigslist.org', 'quito.craigslist.org',
#          'elsalvador.craigslist.org', 'guatemala.craigslist.org', 'acapulco.craigslist.com.mx',
#          'bajasur.craigslist.com.mx', 'chihuahua.craigslist.com.mx', 'juarez.craigslist.com.mx',
#          'guadalajara.craigslist.com.mx', 'guanajuato.craigslist.com.mx', 'hermosillo.craigslist.com.mx',
#          'mazatlan.craigslist.com.mx', 'mexicocity.craigslist.com.mx', 'monterrey.craigslist.com.mx',
#          'oaxaca.craigslist.com.mx', 'puebla.craigslist.com.mx', 'pv.craigslist.com.mx', 'tijuana.craigslist.com.mx',
#          'veracruz.craigslist.com.mx', 'yucatan.craigslist.com.mx', 'managua.craigslist.org', 'panama.craigslist.org',
#          'lima.craigslist.org', 'puertorico.craigslist.org', 'montevideo.craigslist.org', 'caracas.craigslist.org',
#          'virgin.craigslist.org', 'cairo.craigslist.org', 'addisababa.craigslist.org', 'accra.craigslist.org',
#          'kenya.craigslist.org', 'casablanca.craigslist.org', 'capetown.craigslist.co.za', 'durban.craigslist.co.za',
#          'johannesburg.craigslist.co.za', 'pretoria.craigslist.co.za', 'tunis.craigslist.org']
#
# print(len(links))
# count = 0
# for text in link_texts:
#     if text.isupper():
#         count += 1
# print(count + len(links))
#
# count = 0
# for text in link_texts:
#     pos = link_texts.index(text)
#     if text.isupper():
#         count += 1
#     else:
#         print(text + ': ' + links[pos - count])
#
# from random import choice
# location = choice(link_texts)
# # while location.isupper():
# #     location = choice(link_texts)
# location_pos = link_texts.index(location)
# link_texts_slice = link_texts[:location_pos + 1]
# print(link_texts_slice)
# count = 0
# for texts in link_texts_slice:
#     if texts.isupper():
#         count += 1
# link = links[location_pos - count]
# print(location_pos, location, link)


data_ids = "3:00202_6RMSoTILbQUz_0d20jt,3:00n0n_1XXJYVND5vlz_0cC09u,3:00e0e_kR9nD38gqDAz_0dP0b3,3:00W0W_b9hT8l9CSHAz_05M074,3:00505_iIZ3GYwXTWPz_0oQ0ic,3:00d0d_uTEPRUvQE7z_0lM0t2,3:00505_gFflfHA9HpRz_0CI0sx,3:00w0w_iQWmkCfpwMsz_0qd0jj,3:00V0V_k03gLtlVzZpz_0lM0t2,3:00C0C_g2bcjSMVkj4z_0Ar0t2,3:00000_8XOaIGShsSvz_0fu0bW,3:00S0S_dHxTYNwuO0gz_0lM0t2,3:00K0K_6BmVxdzZV6Xz_0CI0ri,3:00a0a_evn3YlS6vGhz_0BL0t2,3:00v0v_c6XXPNJnya2z_0CI0mJ,3:00d0d_edXz27tX4NHz_0CI0nW,3:00707_K4p3zwEpe0z_0Bu0t2,3:00d0d_1c9RcvlBELpz_0A60t2,3:00r0r_cS0WTGrQFdpz_0wj0pj,3:00I0I_4U3Xy5uJNxGz_0tn0kF,3:00E0E_kwIFUzcaxU3z_0lM0t2,3:00L0L_6B3YBQ62o2Pz_0yZ0t2,3:00y0y_l3yAAWMfcK5z_0uf0r2,3:01212_4HmngLUyV1Yz_0lM0t2"
data_ids = data_ids.split(',')
print(data_ids)
for id in data_ids:
    data_ids[data_ids.index(id)] = id.split(':')[1]
print(data_ids)
# Nothing found for that search. (All words must match.)
# Zero local results found. Here are some from nearby areas. Checking 'include nearby areas' will expand your search.