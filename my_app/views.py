import random
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from . import models

# Create your views here.
driver = webdriver.Chrome(executable_path=r'C:/Users/acer/Downloads/chromedriver_win32/chromedriver.exe')
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/d/housing/search/hhh?sort=upcoming&query=ping%20pong'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/jjj?sort=rel&query=ping+pong'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/d/for-sale/search/sss?sort=priceasc&query=ping%20pong'
# BASE_CRAIGSLIST_URL = 'https://www.yellowproxy.net/browse.php?u=https%3A%2F%2Flosangeles.craigslist.org%2Fd%2Ffor-sale%2Fsearch%2Fhhh%3Fquery%3D{}%26sort%3Drel&b=4&f=norefer'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/sss?query=ping+pong&sort=priceasc&purveyor-input=all&min_price=10&max_price=200'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/sss?query=ping+pong&sort=priceasc&purveyor-input=all&min_price=25'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/sss?query=ping+pong&sort=priceasc&purveyor-input=all&max_price=300'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/sss?query=ping+pong&sort=rel&purveyor-input=all&min_price=0&max_price=0'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/sss?query=ping+pong&sort=rel&purveyor-input=all&min_price=&max_price='    WHEN I ENTERED JAGONS
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/sss?query=ping+pong&sort=priceasc&purveyor-input=all&min_price=0&max_price=1000'

# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/hhh?query=apartment&sort=rel&min_bedrooms=2&max_bedrooms=4&availabilityMode=0&sale_date=all+dates'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/hhh?query=apartment&sort=rel&min_price=2000&max_price=4000&min_bedrooms=2&max_bedrooms=4&availabilityMode=0&sale_date=all+dates'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/hhh?query=apartment&sort=rel&min_price=2000&max_price=4000&min_bedrooms=2&max_bedrooms=4&min_bathrooms=2&max_bathrooms=5&availabilityMode=0&sale_date=all+dates'
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/hhh?query=apartment&sort=rel&min_price=2000&max_price=4000&min_bedrooms=2&max_bedrooms=4&min_bathrooms=2&max_bathrooms=5'

# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/d/{}/search/{}?sort={}&query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    links = ['', '', 'auburn.craigslist.org', 'bham.craigslist.org', 'dothan.craigslist.org', 'shoals.craigslist.org',
             'gadsden.craigslist.org', 'huntsville.craigslist.org', 'mobile.craigslist.org',
             'montgomery.craigslist.org', 'tuscaloosa.craigslist.org', '', 'anchorage.craigslist.org',
             'fairbanks.craigslist.org', 'kenai.craigslist.org', 'juneau.craigslist.org', '',
             'flagstaff.craigslist.org', 'mohave.craigslist.org', 'phoenix.craigslist.org', 'prescott.craigslist.org',
             'showlow.craigslist.org', 'sierravista.craigslist.org', 'tucson.craigslist.org', 'yuma.craigslist.org', '',
             'fayar.craigslist.org', 'fortsmith.craigslist.org', 'jonesboro.craigslist.org',
             'littlerock.craigslist.org', 'texarkana.craigslist.org', '', 'bakersfield.craigslist.org',
             'chico.craigslist.org', 'fresno.craigslist.org', 'goldcountry.craigslist.org', 'hanford.craigslist.org',
             'humboldt.craigslist.org', 'imperial.craigslist.org', 'inlandempire.craigslist.org',
             'losangeles.craigslist.org', 'mendocino.craigslist.org', 'merced.craigslist.org', 'modesto.craigslist.org',
             'monterey.craigslist.org', 'orangecounty.craigslist.org', 'palmsprings.craigslist.org',
             'redding.craigslist.org', 'sacramento.craigslist.org', 'sandiego.craigslist.org', 'sfbay.craigslist.org',
             'slo.craigslist.org', 'santabarbara.craigslist.org', 'santamaria.craigslist.org',
             'siskiyou.craigslist.org', 'stockton.craigslist.org', 'susanville.craigslist.org',
             'ventura.craigslist.org', 'visalia.craigslist.org', 'yubasutter.craigslist.org', '',
             'boulder.craigslist.org', 'cosprings.craigslist.org', 'denver.craigslist.org', 'eastco.craigslist.org',
             'fortcollins.craigslist.org', 'rockies.craigslist.org', 'pueblo.craigslist.org',
             'westslope.craigslist.org', '', 'newlondon.craigslist.org', 'hartford.craigslist.org',
             'newhaven.craigslist.org', 'nwct.craigslist.org', '', 'delaware.craigslist.org', '',
             'washingtondc.craigslist.org', '', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fbrw',
             'daytona.craigslist.org', 'keys.craigslist.org', 'fortlauderdale.craigslist.org',
             'fortmyers.craigslist.org', 'gainesville.craigslist.org', 'cfl.craigslist.org',
             'jacksonville.craigslist.org', 'lakeland.craigslist.org',
             '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc', 'lakecity.craigslist.org', 'ocala.craigslist.org',
             'okaloosa.craigslist.org', 'orlando.craigslist.org', 'panamacity.craigslist.org',
             'pensacola.craigslist.org', 'sarasota.craigslist.org', 'miami.craigslist.org', 'spacecoast.craigslist.org',
             'staugustine.craigslist.org', 'tallahassee.craigslist.org', 'tampa.craigslist.org',
             'treasure.craigslist.org', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc', '',
             'albanyga.craigslist.org', 'athensga.craigslist.org', 'atlanta.craigslist.org', 'augusta.craigslist.org',
             'brunswick.craigslist.org', 'columbusga.craigslist.org', 'macon.craigslist.org', 'nwga.craigslist.org',
             'savannah.craigslist.org', 'statesboro.craigslist.org', 'valdosta.craigslist.org', '',
             'honolulu.craigslist.org', '', 'boise.craigslist.org', 'eastidaho.craigslist.org',
             'lewiston.craigslist.org', 'twinfalls.craigslist.org', '', 'bn.craigslist.org', 'chambana.craigslist.org',
             'chicago.craigslist.org', 'decatur.craigslist.org', 'lasalle.craigslist.org', 'mattoon.craigslist.org',
             'peoria.craigslist.org', 'rockford.craigslist.org', 'carbondale.craigslist.org',
             'springfieldil.craigslist.org', 'quincy.craigslist.org', '', 'bloomington.craigslist.org',
             'evansville.craigslist.org', 'fortwayne.craigslist.org', 'indianapolis.craigslist.org',
             'kokomo.craigslist.org', 'tippecanoe.craigslist.org', 'muncie.craigslist.org', 'richmondin.craigslist.org',
             'southbend.craigslist.org', 'terrehaute.craigslist.org', '', 'ames.craigslist.org',
             'cedarrapids.craigslist.org', 'desmoines.craigslist.org', 'dubuque.craigslist.org',
             'fortdodge.craigslist.org', 'iowacity.craigslist.org', 'masoncity.craigslist.org',
             'quadcities.craigslist.org', 'siouxcity.craigslist.org', 'ottumwa.craigslist.org',
             'waterloo.craigslist.org', '', 'lawrence.craigslist.org', 'ksu.craigslist.org', 'nwks.craigslist.org',
             'salina.craigslist.org', 'seks.craigslist.org', 'swks.craigslist.org', 'topeka.craigslist.org',
             'wichita.craigslist.org', '', 'bgky.craigslist.org', 'eastky.craigslist.org', 'lexington.craigslist.org',
             'louisville.craigslist.org', 'owensboro.craigslist.org', 'westky.craigslist.org', '',
             'batonrouge.craigslist.org', 'cenla.craigslist.org', 'houma.craigslist.org', 'lafayette.craigslist.org',
             'lakecharles.craigslist.org', 'monroe.craigslist.org', 'neworleans.craigslist.org',
             'shreveport.craigslist.org', '', 'maine.craigslist.org', '', 'annapolis.craigslist.org',
             'baltimore.craigslist.org', 'easternshore.craigslist.org', 'frederick.craigslist.org',
             'smd.craigslist.org', 'westmd.craigslist.org', '', 'boston.craigslist.org', 'capecod.craigslist.org',
             'southcoast.craigslist.org', 'westernmass.craigslist.org', 'worcester.craigslist.org', '',
             'annarbor.craigslist.org', 'battlecreek.craigslist.org', 'centralmich.craigslist.org',
             'detroit.craigslist.org', 'flint.craigslist.org', 'grandrapids.craigslist.org', 'holland.craigslist.org',
             'jxn.craigslist.org', 'kalamazoo.craigslist.org', 'lansing.craigslist.org', 'monroemi.craigslist.org',
             'muskegon.craigslist.org', 'nmi.craigslist.org', 'porthuron.craigslist.org', 'saginaw.craigslist.org',
             'swmi.craigslist.org', 'thumb.craigslist.org', 'up.craigslist.org', '', 'bemidji.craigslist.org',
             'brainerd.craigslist.org', 'duluth.craigslist.org', 'mankato.craigslist.org', 'minneapolis.craigslist.org',
             'rmn.craigslist.org', 'marshall.craigslist.org', 'stcloud.craigslist.org', '', 'gulfport.craigslist.org',
             'hattiesburg.craigslist.org', 'jackson.craigslist.org', 'meridian.craigslist.org',
             'northmiss.craigslist.org', 'natchez.craigslist.org', '', 'columbiamo.craigslist.org',
             'joplin.craigslist.org', 'kansascity.craigslist.org', 'kirksville.craigslist.org', 'loz.craigslist.org',
             'semo.craigslist.org', 'springfield.craigslist.org', 'stjoseph.craigslist.org', 'stlouis.craigslist.org',
             '', 'billings.craigslist.org', 'bozeman.craigslist.org', 'butte.craigslist.org',
             'greatfalls.craigslist.org', 'helena.craigslist.org', 'kalispell.craigslist.org',
             'missoula.craigslist.org', 'montana.craigslist.org', '', 'grandisland.craigslist.org',
             'lincoln.craigslist.org', 'northplatte.craigslist.org', 'omaha.craigslist.org',
             'scottsbluff.craigslist.org', '', 'elko.craigslist.org', 'lasvegas.craigslist.org', 'reno.craigslist.org',
             '', 'nh.craigslist.org', '', 'cnj.craigslist.org', 'jerseyshore.craigslist.org',
             'newjersey.craigslist.org', 'southjersey.craigslist.org', '', 'albuquerque.craigslist.org',
             'clovis.craigslist.org', 'farmington.craigslist.org', 'lascruces.craigslist.org', 'roswell.craigslist.org',
             'santafe.craigslist.org', '', 'albany.craigslist.org', 'binghamton.craigslist.org',
             'buffalo.craigslist.org', 'catskills.craigslist.org', 'chautauqua.craigslist.org', 'elmira.craigslist.org',
             'fingerlakes.craigslist.org', 'glensfalls.craigslist.org', 'hudsonvalley.craigslist.org',
             'ithaca.craigslist.org', 'longisland.craigslist.org', 'newyork.craigslist.org', 'oneonta.craigslist.org',
             'plattsburgh.craigslist.org', 'potsdam.craigslist.org', 'rochester.craigslist.org',
             'syracuse.craigslist.org', 'twintiers.craigslist.org', 'utica.craigslist.org', 'watertown.craigslist.org',
             '', 'asheville.craigslist.org', 'boone.craigslist.org', 'charlotte.craigslist.org',
             'eastnc.craigslist.org', 'fayetteville.craigslist.org', 'greensboro.craigslist.org',
             'hickory.craigslist.org', 'onslow.craigslist.org', 'outerbanks.craigslist.org', 'raleigh.craigslist.org',
             'wilmington.craigslist.org', 'winstonsalem.craigslist.org', '', 'bismarck.craigslist.org',
             'fargo.craigslist.org', 'grandforks.craigslist.org', 'nd.craigslist.org', '', 'akroncanton.craigslist.org',
             'ashtabula.craigslist.org', 'athensohio.craigslist.org', 'chillicothe.craigslist.org',
             'cincinnati.craigslist.org', 'cleveland.craigslist.org', 'columbus.craigslist.org',
             'dayton.craigslist.org', 'limaohio.craigslist.org', 'mansfield.craigslist.org', 'sandusky.craigslist.org',
             'toledo.craigslist.org', 'tuscarawas.craigslist.org', 'youngstown.craigslist.org',
             'zanesville.craigslist.org', '', 'lawton.craigslist.org', 'enid.craigslist.org',
             'oklahomacity.craigslist.org', 'stillwater.craigslist.org', 'tulsa.craigslist.org', '',
             'bend.craigslist.org', 'corvallis.craigslist.org', 'eastoregon.craigslist.org', 'eugene.craigslist.org',
             'klamath.craigslist.org', 'medford.craigslist.org', 'oregoncoast.craigslist.org',
             'portland.craigslist.org', 'roseburg.craigslist.org', 'salem.craigslist.org', '', 'altoona.craigslist.org',
             'chambersburg.craigslist.org', 'erie.craigslist.org', 'harrisburg.craigslist.org',
             'lancaster.craigslist.org', 'allentown.craigslist.org', 'meadville.craigslist.org',
             'philadelphia.craigslist.org', 'pittsburgh.craigslist.org', 'poconos.craigslist.org',
             'reading.craigslist.org', 'scranton.craigslist.org', 'pennstate.craigslist.org',
             'williamsport.craigslist.org', 'york.craigslist.org', '', 'providence.craigslist.org', '',
             'charleston.craigslist.org', 'columbia.craigslist.org', 'florencesc.craigslist.org',
             'greenville.craigslist.org', 'hiltonhead.craigslist.org', 'myrtlebeach.craigslist.org', '',
             'nesd.craigslist.org', 'csd.craigslist.org', 'rapidcity.craigslist.org', 'siouxfalls.craigslist.org',
             'sd.craigslist.org', '', 'chattanooga.craigslist.org', 'clarksville.craigslist.org',
             'cookeville.craigslist.org', 'jacksontn.craigslist.org', 'knoxville.craigslist.org',
             'memphis.craigslist.org', 'nashville.craigslist.org', 'tricities.craigslist.org', '',
             'abilene.craigslist.org', 'amarillo.craigslist.org', 'austin.craigslist.org', 'beaumont.craigslist.org',
             'brownsville.craigslist.org', 'collegestation.craigslist.org', 'corpuschristi.craigslist.org',
             'dallas.craigslist.org', 'nacogdoches.craigslist.org', 'delrio.craigslist.org', 'elpaso.craigslist.org',
             'galveston.craigslist.org', 'houston.craigslist.org', 'killeen.craigslist.org', 'laredo.craigslist.org',
             'lubbock.craigslist.org', 'mcallen.craigslist.org', 'odessa.craigslist.org', 'sanangelo.craigslist.org',
             'sanantonio.craigslist.org', 'sanmarcos.craigslist.org', 'bigbend.craigslist.org', 'texoma.craigslist.org',
             'easttexas.craigslist.org', 'victoriatx.craigslist.org', 'waco.craigslist.org',
             'wichitafalls.craigslist.org', '', 'logan.craigslist.org', 'ogden.craigslist.org', 'provo.craigslist.org',
             'saltlakecity.craigslist.org', 'stgeorge.craigslist.org', '', 'vermont.craigslist.org', '',
             'charlottesville.craigslist.org', 'danville.craigslist.org', 'fredericksburg.craigslist.org',
             'norfolk.craigslist.org', 'harrisonburg.craigslist.org', 'lynchburg.craigslist.org',
             'blacksburg.craigslist.org', 'richmond.craigslist.org', 'roanoke.craigslist.org', 'swva.craigslist.org',
             'winchester.craigslist.org', '', 'bellingham.craigslist.org', 'kpr.craigslist.org',
             'moseslake.craigslist.org', 'olympic.craigslist.org', 'pullman.craigslist.org', 'seattle.craigslist.org',
             'skagit.craigslist.org', 'spokane.craigslist.org', 'wenatchee.craigslist.org', 'yakima.craigslist.org', '',
             'charlestonwv.craigslist.org', 'martinsburg.craigslist.org', 'huntington.craigslist.org',
             'morgantown.craigslist.org', 'wheeling.craigslist.org', 'parkersburg.craigslist.org', 'swv.craigslist.org',
             'wv.craigslist.org', '', 'appleton.craigslist.org', 'eauclaire.craigslist.org', 'greenbay.craigslist.org',
             'janesville.craigslist.org', 'racine.craigslist.org', 'lacrosse.craigslist.org', 'madison.craigslist.org',
             'milwaukee.craigslist.org', 'northernwi.craigslist.org', 'sheboygan.craigslist.org',
             'wausau.craigslist.org', '', 'wyoming.craigslist.org', '', 'micronesia.craigslist.org',
             'puertorico.craigslist.org', 'virgin.craigslist.org', 'calgary.craigslist.org', '',
             'edmonton.craigslist.org', 'ftmcmurray.craigslist.org', 'lethbridge.craigslist.org', 'hat.craigslist.org',
             'peace.craigslist.org', 'reddeer.craigslist.org', 'cariboo.craigslist.org', '',
             'comoxvalley.craigslist.org', 'abbotsford.craigslist.org', 'kamloops.craigslist.org',
             'kelowna.craigslist.org', 'kootenays.craigslist.org', 'nanaimo.craigslist.org',
             'princegeorge.craigslist.org', 'skeena.craigslist.org', 'sunshine.craigslist.org',
             'vancouver.craigslist.org', 'victoria.craigslist.org', 'whistler.craigslist.org',
             'winnipeg.craigslist.org', '', 'newbrunswick.craigslist.org', '', 'newfoundland.craigslist.org', '',
             'territories.craigslist.org', '', 'yellowknife.craigslist.org', 'halifax.craigslist.org', '',
             'barrie.craigslist.org', '', 'belleville.craigslist.org', 'brantford.craigslist.org',
             'chatham.craigslist.org', 'cornwall.craigslist.org', 'guelph.craigslist.org', 'hamilton.craigslist.org',
             'kingston.craigslist.org', 'kitchener.craigslist.org', 'londonon.craigslist.org', 'niagara.craigslist.org',
             'ottawa.craigslist.org', 'owensound.craigslist.org', 'peterborough.craigslist.org',
             'sarnia.craigslist.org', 'soo.craigslist.org', 'sudbury.craigslist.org', 'thunderbay.craigslist.org',
             'toronto.craigslist.org', 'windsor.craigslist.org', 'pei.craigslist.org', '', 'montreal.craigslist.org',
             '', 'quebec.craigslist.org', 'saguenay.craigslist.org', 'sherbrooke.craigslist.org',
             'troisrivieres.craigslist.org', '', '', 'regina.craigslist.org', 'saskatoon.craigslist.org', '',
             'whitehorse.craigslist.org', 'vienna.craigslist.at', '', 'brussels.craigslist.org', '',
             'bulgaria.craigslist.org', '', 'zagreb.craigslist.org', '', 'prague.craigslist.cz', '',
             'copenhagen.craigslist.org', '', 'helsinki.craigslist.fi', '', 'bordeaux.craigslist.org', '',
             'rennes.craigslist.org', 'grenoble.craigslist.org', 'lille.craigslist.org', 'loire.craigslist.org',
             'lyon.craigslist.org', 'marseilles.craigslist.org', 'montpellier.craigslist.org',
             'cotedazur.craigslist.org', 'rouen.craigslist.org', 'paris.craigslist.org', 'strasbourg.craigslist.org',
             'toulouse.craigslist.org', 'berlin.craigslist.de', '', 'bremen.craigslist.de', 'cologne.craigslist.de',
             'dresden.craigslist.de', 'dusseldorf.craigslist.de', 'essen.craigslist.de', 'frankfurt.craigslist.de',
             'hamburg.craigslist.de', 'hannover.craigslist.de', 'heidelberg.craigslist.de',
             'kaiserslautern.craigslist.de', 'leipzig.craigslist.de', 'munich.craigslist.de', 'nuremberg.craigslist.de',
             'stuttgart.craigslist.de', 'athens.craigslist.gr', '', 'budapest.craigslist.org', '',
             'reykjavik.craigslist.org', '', 'dublin.craigslist.org', '', 'bologna.craigslist.it', '',
             'florence.craigslist.it', 'genoa.craigslist.it', 'milan.craigslist.it', 'naples.craigslist.it',
             'perugia.craigslist.it', 'rome.craigslist.it', 'sardinia.craigslist.it', 'sicily.craigslist.it',
             'torino.craigslist.it', 'venice.craigslist.it', 'luxembourg.craigslist.org', '',
             'amsterdam.craigslist.org', '', 'oslo.craigslist.org', '', 'warsaw.craigslist.pl', '',
             'faro.craigslist.pt', '', 'lisbon.craigslist.pt', 'porto.craigslist.pt', 'bucharest.craigslist.org', '',
             'moscow.craigslist.org', '', 'stpetersburg.craigslist.org', 'alicante.craigslist.es', '',
             'baleares.craigslist.es', 'barcelona.craigslist.es', 'bilbao.craigslist.es', '', 'cadiz.craigslist.es',
             'canarias.craigslist.es', 'granada.craigslist.es', 'madrid.craigslist.es', 'malaga.craigslist.es',
             'sevilla.craigslist.es', 'valencia.craigslist.es', '', 'stockholm.craigslist.se', '',
             'basel.craigslist.ch', 'bern.craigslist.ch', 'geneva.craigslist.ch', 'lausanne.craigslist.ch',
             'zurich.craigslist.ch', '', 'istanbul.craigslist.com.tr', '', 'ukraine.craigslist.org', '',
             'aberdeen.craigslist.co.uk', 'bath.craigslist.co.uk', 'belfast.craigslist.co.uk',
             'birmingham.craigslist.co.uk', 'brighton.craigslist.co.uk', 'bristol.craigslist.co.uk',
             'cambridge.craigslist.co.uk', 'cardiff.craigslist.co.uk', 'coventry.craigslist.co.uk',
             'derby.craigslist.co.uk', 'devon.craigslist.co.uk', 'dundee.craigslist.co.uk', 'norwich.craigslist.co.uk',
             'eastmids.craigslist.co.uk', 'edinburgh.craigslist.co.uk', 'essex.craigslist.co.uk',
             'glasgow.craigslist.co.uk', 'hampshire.craigslist.co.uk', 'kent.craigslist.co.uk',
             'leeds.craigslist.co.uk', 'liverpool.craigslist.co.uk', 'london.craigslist.co.uk',
             'manchester.craigslist.co.uk', 'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk',
             'oxford.craigslist.co.uk', 'sheffield.craigslist.co.uk', 'bangladesh.craigslist.org', '',
             'beijing.craigslist.com.cn', '', 'chengdu.craigslist.com.cn', 'chongqing.craigslist.com.cn',
             'dalian.craigslist.com.cn', 'guangzhou.craigslist.com.cn', 'hangzhou.craigslist.com.cn',
             'nanjing.craigslist.com.cn', 'shanghai.craigslist.com.cn', 'shenyang.craigslist.com.cn',
             'shenzhen.craigslist.com.cn', 'wuhan.craigslist.com.cn', 'xian.craigslist.com.cn',
             'micronesia.craigslist.org', '', 'hongkong.craigslist.hk', '', 'ahmedabad.craigslist.co.in', '',
             'bangalore.craigslist.co.in', 'bhubaneswar.craigslist.co.in', 'chandigarh.craigslist.co.in',
             'chennai.craigslist.co.in', 'delhi.craigslist.co.in', 'goa.craigslist.co.in', 'hyderabad.craigslist.co.in',
             'indore.craigslist.co.in', 'jaipur.craigslist.co.in', 'kerala.craigslist.co.in',
             'kolkata.craigslist.co.in', 'lucknow.craigslist.co.in', 'mumbai.craigslist.co.in', 'pune.craigslist.co.in',
             'surat.craigslist.co.in', 'jakarta.craigslist.org', '', 'tehran.craigslist.org', '',
             'baghdad.craigslist.org', '', 'haifa.craigslist.org', '', 'jerusalem.craigslist.org',
             'telaviv.craigslist.org', 'ramallah.craigslist.org', 'fukuoka.craigslist.jp', '',
             'hiroshima.craigslist.jp', 'nagoya.craigslist.jp', 'okinawa.craigslist.jp', 'osaka.craigslist.jp',
             'sapporo.craigslist.jp', 'sendai.craigslist.jp', 'tokyo.craigslist.jp', 'seoul.craigslist.co.kr', '',
             'kuwait.craigslist.org', '', 'beirut.craigslist.org', '', 'malaysia.craigslist.org', '',
             'pakistan.craigslist.org', '', 'bacolod.craigslist.com.ph', '', 'naga.craigslist.com.ph',
             'cdo.craigslist.com.ph', 'cebu.craigslist.com.ph', 'davaocity.craigslist.com.ph',
             'iloilo.craigslist.com.ph', 'manila.craigslist.com.ph', 'pampanga.craigslist.com.ph',
             'zamboanga.craigslist.com.ph', 'singapore.craigslist.com.sg', '', 'taipei.craigslist.com.tw', '',
             'bangkok.craigslist.co.th', '', 'dubai.craigslist.org', '', 'vietnam.craigslist.org', '',
             'adelaide.craigslist.com.au', 'brisbane.craigslist.com.au', '', 'cairns.craigslist.com.au',
             'canberra.craigslist.com.au', 'darwin.craigslist.com.au', 'goldcoast.craigslist.com.au',
             'melbourne.craigslist.com.au', 'ntl.craigslist.com.au', 'perth.craigslist.com.au',
             'sydney.craigslist.com.au', 'hobart.craigslist.com.au', 'wollongong.craigslist.com.au',
             'auckland.craigslist.org', 'christchurch.craigslist.org', '', 'dunedin.craigslist.co.nz',
             'wellington.craigslist.org', 'buenosaires.craigslist.org', 'lapaz.craigslist.org',
             'belohorizonte.craigslist.org', '', 'brasilia.craigslist.org', '', 'curitiba.craigslist.org', '',
             'fortaleza.craigslist.org', 'portoalegre.craigslist.org', 'recife.craigslist.org', 'rio.craigslist.org',
             'salvador.craigslist.org', '', 'saopaulo.craigslist.org', 'caribbean.craigslist.org',
             'santiago.craigslist.org', '', 'colombia.craigslist.org', '', 'costarica.craigslist.org', '',
             'santodomingo.craigslist.org', '', 'quito.craigslist.org', '', 'elsalvador.craigslist.org', '',
             'guatemala.craigslist.org', '', 'acapulco.craigslist.com.mx', '', 'bajasur.craigslist.com.mx', '',
             'chihuahua.craigslist.com.mx', 'juarez.craigslist.com.mx', 'guadalajara.craigslist.com.mx',
             'guanajuato.craigslist.com.mx', 'hermosillo.craigslist.com.mx', 'mazatlan.craigslist.com.mx',
             'mexicocity.craigslist.com.mx', 'monterrey.craigslist.com.mx', 'oaxaca.craigslist.com.mx',
             'puebla.craigslist.com.mx', 'pv.craigslist.com.mx', 'tijuana.craigslist.com.mx',
             'veracruz.craigslist.com.mx', 'yucatan.craigslist.com.mx', 'managua.craigslist.org',
             'panama.craigslist.org', '', 'lima.craigslist.org', '', 'puertorico.craigslist.org', '',
             'montevideo.craigslist.org', '', 'caracas.craigslist.org', '', 'virgin.craigslist.org', '',
             'cairo.craigslist.org', '', 'addisababa.craigslist.org', 'accra.craigslist.org', '',
             'kenya.craigslist.org', '', 'casablanca.craigslist.org', '', 'capetown.craigslist.co.za', '',
             'durban.craigslist.co.za', '', 'johannesburg.craigslist.co.za', '', 'pretoria.craigslist.co.za',
             'tunis.craigslist.org', '', '', '', '']
    link_texts = ['US', 'ALABAMA', 'Auburn', 'Birmingham', 'Dothan', 'Florence / Muscle Shoals', 'Gadsden-Anniston',
                  'Huntsville / Decatur', 'Mobile', 'Montgomery', 'Tuscaloosa', 'ALASKA', 'Anchorage / Mat-Su',
                  'Fairbanks', 'Kenai Peninsula', 'Southeast Alaska', 'ARIZONA', 'Flagstaff / Sedona', 'Mohave County',
                  'Phoenix', 'Prescott', 'Show Low', 'Sierra Vista', 'Tucson', 'Yuma', 'ARKANSAS', 'Fayetteville ',
                  'Fort Smith', 'Jonesboro', 'Little Rock', 'Texarkana', 'CALIFORNIA', 'Bakersfield', 'Chico',
                  'Fresno / Madera', 'Gold Country', 'Hanford-Corcoran', 'Humboldt County', 'Imperial County',
                  'Inland Empire', 'Los Angeles', 'Mendocino County', 'Merced', 'Modesto', 'Monterey Bay',
                  'Orange County', 'Palm Springs', 'Redding', 'Sacramento', 'San Diego', 'San Francisco Bay Area',
                  'San Luis Obispo', 'Santa Barbara', 'Santa Maria', 'Siskiyou County', 'Stockton', 'Susanville',
                  'Ventura County', 'Visalia-Tulare', 'Yuba-Sutter', 'COLORADO', 'Boulder', 'Colorado Springs',
                  'Denver', 'Eastern CO', 'Fort Collins / North CO', 'High Rockies', 'Pueblo', 'Western Slope',
                  'CONNECTICUT', 'Eastern CT', 'Hartford', 'New Haven', 'Northwest Ct', 'DELAWARE', 'Delaware',
                  'DISTRICT OF COLUMBIA', 'Washington', 'FLORIDA', 'Broward County', 'Daytona Beach', 'Florida Keys',
                  'Fort Lauderdale', 'Ft Myers / Sw Florida', 'Gainesville', 'Heartland Florida', 'Jacksonville',
                  'Lakeland', 'Miami / Dade', 'North Central FL', 'Ocala', 'Okaloosa / Walton', 'Orlando',
                  'Panama City', 'Pensacola', 'Sarasota-Bradenton', 'South Florida', 'Space Coast', 'St Augustine',
                  'Tallahassee', 'Tampa Bay Area', 'Treasure Coast', 'Palm Beach County', 'GEORGIA', 'Albany ',
                  'Athens', 'Atlanta', 'Augusta', 'Brunswick', 'Columbus ', 'Macon / Warner Robins', 'Northwest GA',
                  'Savannah / Hinesville', 'Statesboro', 'Valdosta', 'HAWAII', 'Hawaii', 'IDAHO', 'Boise', 'East Idaho',
                  'Lewiston / Clarkston', 'Twin Falls', 'ILLINOIS', 'Bloomington-Normal', 'Champaign Urbana', 'Chicago',
                  'Decatur', 'La Salle Co', 'Mattoon-Charleston', 'Peoria', 'Rockford', 'Southern Illinois',
                  'Springfield ', 'Western IL', 'INDIANA', 'Bloomington', 'Evansville', 'Fort Wayne', 'Indianapolis',
                  'Kokomo', 'Lafayette / West Lafayette', 'Muncie / Anderson', 'Richmond ', 'South Bend / Michiana',
                  'Terre Haute', 'IOWA', 'Ames', 'Cedar Rapids', 'Des Moines', 'Dubuque', 'Fort Dodge', 'Iowa City',
                  'Mason City', 'Quad Cities', 'Sioux City', 'Southeast IA', 'Waterloo / Cedar Falls', 'KANSAS',
                  'Lawrence', 'Manhattan', 'Northwest KS', 'Salina', 'Southeast KS', 'Southwest KS', 'Topeka',
                  'Wichita', 'KENTUCKY', 'Bowling Green', 'Eastern Kentucky', 'Lexington', 'Louisville', 'Owensboro',
                  'Western KY', 'LOUISIANA', 'Baton Rouge', 'Central Louisiana', 'Houma', 'Lafayette', 'Lake Charles',
                  'Monroe', 'New Orleans', 'Shreveport', 'MAINE', 'Maine', 'MARYLAND', 'Annapolis', 'Baltimore',
                  'Eastern Shore', 'Frederick', 'Southern Maryland', 'Western Maryland', 'MASSACHUSETTS', 'Boston',
                  'Cape Cod / Islands', 'South Coast', 'Western Massachusetts', 'Worcester / Central MA', 'MICHIGAN',
                  'Ann Arbor', 'Battle Creek', 'Central Michigan', 'Detroit Metro', 'Flint', 'Grand Rapids', 'Holland',
                  'Jackson ', 'Kalamazoo', 'Lansing', 'Monroe ', 'Muskegon', 'Northern Michigan', 'Port Huron',
                  'Saginaw-Midland-Baycity', 'Southwest Michigan', 'The Thumb', 'Upper Peninsula', 'MINNESOTA',
                  'Bemidji', 'Brainerd', 'Duluth / Superior', 'Mankato', 'Minneapolis / St Paul', 'Rochester ',
                  'Southwest MN', 'St Cloud', 'MISSISSIPPI', 'Gulfport / Biloxi', 'Hattiesburg', 'Jackson', 'Meridian',
                  'North Mississippi', 'Southwest MS', 'MISSOURI', 'Columbia / Jeff City', 'Joplin', 'Kansas City',
                  'Kirksville', 'Lake Of The Ozarks', 'Southeast Missouri', 'Springfield', 'St Joseph', 'St Louis',
                  'MONTANA', 'Billings', 'Bozeman', 'Butte', 'Great Falls', 'Helena', 'Kalispell', 'Missoula',
                  'Eastern Montana', 'NEBRASKA', 'Grand Island', 'Lincoln', 'North Platte', 'Omaha / Council Bluffs',
                  'Scottsbluff / Panhandle', 'NEVADA', 'Elko', 'Las Vegas', 'Reno / Tahoe', 'NEW HAMPSHIRE',
                  'New Hampshire', 'NEW JERSEY', 'Central NJ', 'Jersey Shore', 'North Jersey', 'South Jersey',
                  'NEW MEXICO', 'Albuquerque', 'Clovis / Portales', 'Farmington', 'Las Cruces', 'Roswell / Carlsbad',
                  'Santa Fe / Taos', 'NEW YORK', 'Albany', 'Binghamton', 'Buffalo', 'Catskills', 'Chautauqua',
                  'Elmira-Corning', 'Finger Lakes', 'Glens Falls', 'Hudson Valley', 'Ithaca', 'Long Island',
                  'New York City', 'Oneonta', 'Plattsburgh-Adirondacks', 'Potsdam-Canton-Massena', 'Rochester',
                  'Syracuse', 'Twin Tiers NY/PA', 'Utica-Rome-Oneida', 'Watertown', 'NORTH CAROLINA', 'Asheville',
                  'Boone', 'Charlotte', 'Eastern Nc', 'Fayetteville', 'Greensboro', 'Hickory / Lenoir', 'Jacksonville ',
                  'Outer Banks', 'Raleigh / Durham / CH', 'Wilmington', 'Winston-Salem', 'NORTH DAKOTA', 'Bismarck',
                  'Fargo / Moorhead', 'Grand Forks', 'North Dakota', 'OHIO', 'Akron / Canton', 'Ashtabula', 'Athens ',
                  'Chillicothe', 'Cincinnati', 'Cleveland', 'Columbus', 'Dayton / Springfield', 'Lima / Findlay',
                  'Mansfield', 'Sandusky', 'Toledo', 'Tuscarawas Co', 'Youngstown', 'Zanesville / Cambridge',
                  'OKLAHOMA', 'Lawton', 'Northwest OK', 'Oklahoma City', 'Stillwater', 'Tulsa', 'OREGON', 'Bend',
                  'Corvallis/Albany', 'East Oregon', 'Eugene', 'Klamath Falls', 'Medford-Ashland', 'Oregon Coast',
                  'Portland', 'Roseburg', 'Salem', 'PENNSYLVANIA', 'Altoona-Johnstown', 'Cumberland Valley', 'Erie',
                  'Harrisburg', 'Lancaster', 'Lehigh Valley', 'Meadville', 'Philadelphia', 'Pittsburgh', 'Poconos',
                  'Reading', 'Scranton / Wilkes-Barre', 'State College', 'Williamsport', 'York', 'RHODE ISLAND',
                  'Rhode Island', 'SOUTH CAROLINA', 'Charleston', 'Columbia', 'Florence', 'Greenville / Upstate',
                  'Hilton Head', 'Myrtle Beach', 'SOUTH DAKOTA', 'Northeast SD', 'Pierre / Central SD',
                  'Rapid City / West SD', 'Sioux Falls / Se SD', 'South Dakota', 'TENNESSEE', 'Chattanooga',
                  'Clarksville', 'Cookeville', 'Jackson  ', 'Knoxville', 'Memphis', 'Nashville', 'Tri-Cities', 'TEXAS',
                  'Abilene', 'Amarillo', 'Austin', 'Beaumont / Port Arthur', 'Brownsville', 'College Station',
                  'Corpus Christi', 'Dallas / Fort Worth', 'Deep East Texas', 'Del Rio / Eagle Pass', 'El Paso',
                  'Galveston', 'Houston', 'Killeen / Temple / Ft Hood', 'Laredo', 'Lubbock', 'Mcallen / Edinburg',
                  'Odessa / Midland', 'San Angelo', 'San Antonio', 'San Marcos', 'Southwest TX', 'Texoma',
                  'Tyler / East TX', 'Victoria ', 'Waco', 'Wichita Falls', 'UTAH', 'Logan', 'Ogden-Clearfield',
                  'Provo / Orem', 'Salt Lake City', 'St George', 'VERMONT', 'Vermont', 'VIRGINIA', 'Charlottesville',
                  'Danville', 'Fredericksburg', 'Hampton Roads', 'Harrisonburg', 'Lynchburg', 'New River Valley',
                  'Richmond', 'Roanoke', 'Southwest VA', 'Winchester', 'WASHINGTON', 'Bellingham',
                  'Kennewick-Pasco-Richland', 'Moses Lake', 'Olympic Peninsula', 'Pullman / Moscow', 'Seattle-Tacoma',
                  'Skagit / Island / SJI', "Spokane / Coeur D'Alene", 'Wenatchee', 'Yakima', 'WEST VIRGINIA',
                  'Charleston ', 'Eastern Panhandle', 'Huntington-Ashland', 'Morgantown', 'Northern Panhandle',
                  'Parkersburg-Marietta', 'Southern WV', 'West Virginia (Old)', 'WISCONSIN', 'Appleton-Oshkosh-FDL',
                  'Eau Claire', 'Green Bay', 'Janesville', 'Kenosha-Racine', 'La Crosse', 'Madison', 'Milwaukee',
                  'Northern Wi', 'Sheboygan', 'Wausau', 'WYOMING', 'Wyoming', 'TERRITORIES', 'Guam-Micronesia',
                  'Puerto Rico', 'U.S. Virgin Islands', 'CANADA', 'ALBERTA', 'Calgary', 'Edmonton', 'Ft Mcmurray',
                  'Lethbridge', 'Medicine Hat', 'Peace River Country', 'Red Deer', 'BRITISH COLUMBIA', 'Cariboo',
                  'Comox Valley', 'Fraser Valley', 'Kamloops', 'Kelowna / Okanagan', 'Kootenays', 'Nanaimo',
                  'Prince George', 'Skeena-Bulkley', 'Sunshine Coast', 'Vancouver', 'Victoria', 'Whistler', 'MANITOBA',
                  'Winnipeg', 'NEW BRUNSWICK', 'New Brunswick', 'NEWFOUNDLAND AND LABRADOR', "St John'S",
                  'NORTHWEST TERRITORIES', 'Territories', 'Yellowknife', 'NOVA SCOTIA', 'Halifax', 'ONTARIO', 'Barrie',
                  'Belleville', 'Brantford-Woodstock', 'Chatham-Kent', 'Cornwall', 'Guelph', 'Hamilton-Burlington',
                  'Kingston', 'Kitchener-Waterloo-Cambridge', 'London ', 'Niagara Region', 'Ottawa-Hull-Gatineau',
                  'Owen Sound', 'Peterborough', 'Sarnia', 'Sault Ste Marie', 'Sudbury', 'Thunder Bay', 'Toronto',
                  'Windsor', 'PRINCE EDWARD ISLAND', 'Prince Edward Island', 'QUEBEC', 'Montreal', 'Quebec City',
                  'Saguenay', 'Sherbrooke', 'Trois-Rivieres', 'SASKATCHEWAN', 'Regina', 'Saskatoon', 'YUKON TERRITORY',
                  'Whitehorse', 'EUROPE', 'AUSTRIA', 'Vienna', 'BELGIUM', 'Belgium', 'BULGARIA', 'Bulgaria', 'CROATIA',
                  'Croatia', 'CZECH REPUBLIC', 'Prague', 'DENMARK', 'Copenhagen', 'FINLAND', 'Finland', 'FRANCE',
                  'Bordeaux', 'Brittany', 'Grenoble', 'Lille', 'Loire Valley', 'Lyon', 'Marseille', 'Montpellier',
                  "Nice / Cote D'Azur", 'Normandy', 'Paris', 'Strasbourg', 'Toulouse', 'GERMANY', 'Berlin', 'Bremen',
                  'Cologne', 'Dresden', 'Dusseldorf', 'Essen / Ruhr', 'Frankfurt', 'Hamburg', 'Hannover', 'Heidelberg',
                  'Kaiserslautern', 'Leipzig', 'Munich', 'Nuremberg', 'Stuttgart', 'GREECE', 'Greece', 'HUNGARY',
                  'Budapest', 'ICELAND', 'Reykjavik', 'IRELAND', 'Dublin', 'ITALY', 'Bologna', 'Florence / Tuscany',
                  'Genoa', 'Milan', 'Napoli / Campania', 'Perugia', 'Rome', 'Sardinia', 'Sicilia', 'Torino',
                  'Venice / Veneto', 'LUXEMBOURG', 'Luxembourg', 'NETHERLANDS', 'Amsterdam / Randstad', 'NORWAY',
                  'Norway', 'POLAND', 'Poland', 'PORTUGAL', 'Faro / Algarve', 'Lisbon', 'Porto', 'ROMANIA', 'Romania',
                  'RUSSIAN FEDERATION', 'Moscow', 'St Petersburg', 'SPAIN', 'Alicante', 'Baleares', 'Barcelona',
                  'Bilbao', 'Cadiz', 'Canarias', 'Granada', 'Madrid', 'Malaga', 'Sevilla', 'Valencia', 'SWEDEN',
                  'Sweden', 'SWITZERLAND', 'Basel', 'Bern', 'Geneva', 'Lausanne', 'Zurich', 'TURKEY', 'Turkey',
                  'UKRAINE', 'Ukraine', 'UNITED KINGDOM', 'Aberdeen', 'Bath', 'Belfast', 'Birmingham / West Mids',
                  'Brighton', 'Bristol', 'Cambridge, UK', 'Cardiff / Wales', 'Coventry', 'Derby', 'Devon & Cornwall',
                  'Dundee', 'East Anglia', 'East Midlands', 'Edinburgh', 'Essex', 'Glasgow', 'Hampshire', 'Kent',
                  'Leeds', 'Liverpool', 'London', 'Manchester', 'Newcastle / NE England', 'Nottingham', 'Oxford',
                  'Sheffield', 'ASIA, PACIFIC AND MIDDLE EAST', 'BANGLADESH', 'Bangladesh', 'CHINA', 'Beijing',
                  'Chengdu', 'Chongqing', 'Dalian', 'Guangzhou', 'Hangzhou', 'Nanjing', 'Shanghai', 'Shenyang',
                  'Shenzhen', 'Wuhan', "Xi'An", 'GUAM / MICRONESIA', 'Guam-Micronesia', 'HONG KONG', 'Hong Kong',
                  'INDIA', 'Ahmedabad', 'Bangalore', 'Bhubaneswar', 'Chandigarh', 'Chennai (Madras)', 'Delhi', 'Goa',
                  'Hyderabad', 'Indore', 'Jaipur', 'Kerala', 'Kolkata (Calcutta)', 'Lucknow', 'Mumbai', 'Pune',
                  'Surat Surat', 'INDONESIA', 'Indonesia', 'IRAN', 'Iran', 'IRAQ', 'Iraq', 'ISRAEL AND PALESTINE',
                  'Haifa', 'Jerusalem', 'Tel Aviv', 'West Bank', 'JAPAN', 'Fukuoka', 'Hiroshima', 'Nagoya', 'Okinawa',
                  'Osaka-Kobe-Kyoto', 'Sapporo', 'Sendai', 'Tokyo', 'KOREA', 'Seoul', 'KUWAIT', 'Kuwait', 'LEBANON',
                  'Beirut, Lebanon', 'MALAYSIA', 'Malaysia', 'PAKISTAN', 'Pakistan', 'PHILIPPINES', 'Bacolod',
                  'Bicol Region', 'Cagayan De Oro', 'Cebu', 'Davao City', 'Iloilo', 'Manila', 'Pampanga', 'Zamboanga',
                  'SINGAPORE', 'Singapore', 'TAIWAN', 'Taiwan', 'THAILAND', 'Thailand', 'UNITED ARAB EMIRATES',
                  'United Arab Emirates', 'VIETNAM', 'Vietnam', 'OCEANIA', 'AUSTRALIA', 'Adelaide', 'Brisbane',
                  'Cairns', 'Canberra', 'Darwin', 'Gold Coast', 'Melbourne', 'Newcastle, NSW', 'Perth', 'Sydney',
                  'Tasmania', 'Wollongong', 'NEW ZEALAND', 'Auckland', 'Christchurch', 'Dunedin', 'Wellington',
                  'LATIN AMERICA AND CARIBBEAN', 'ARGENTINA', 'Buenos Aires', 'BOLIVIA', 'Bolivia', 'BRAZIL',
                  'Belo Horizonte', 'Brasilia', 'Curitiba', 'Fortaleza', 'Porto Alegre', 'Recife', 'Rio De Janeiro',
                  'Salvador, Bahia', 'Sao Paulo', 'CARIBBEAN ISLANDS', 'Caribbean Islands', 'CHILE', 'Chile',
                  'COLOMBIA', 'Colombia', 'COSTA RICA', 'Costa Rica', 'DOMINICAN REPUBLIC', 'Dominican Republic',
                  'ECUADOR', 'Ecuador', 'EL SALVADOR', 'El Salvador', 'GUATEMALA', 'Guatemala', 'MEXICO', 'Acapulco',
                  'Baja California Sur', 'Chihuahua', 'Ciudad Juarez', 'Guadalajara', 'Guanajuato', 'Hermosillo',
                  'Mazatlan', 'Mexico City', 'Monterrey', 'Oaxaca', 'Puebla', 'Puerto Vallarta', 'Tijuana', 'Veracruz',
                  'Yucatan', 'NICARAGUA', 'Nicaragua', 'PANAMA', 'Panama', 'PERU', 'Peru', 'PUERTO RICO', 'Puerto Rico',
                  'URUGUAY', 'Montevideo', 'VENEZUELA', 'Venezuela', 'VIRGIN ISLANDS, U.S.', 'Virgin Islands', 'AFRICA',
                  'EGYPT', 'Egypt', 'ETHIOPIA', 'Ethiopia', 'GHANA', 'Ghana', 'KENYA', 'Kenya', 'MOROCCO', 'Morocco',
                  'SOUTH AFRICA', 'Cape Town', 'Durban', 'Johannesburg', 'Pretoria', 'TUNISIA', 'Tunisia']
    headers = ['US', 'CANADA', 'EUROPE', 'ASIA, PACIFIC AND MIDDLE EAST', 'OCEANIA', 'LATIN AMERICA AND CARIBBEAN',
               'AFRICA']
    sub_headers = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE',
                   'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA',
                   'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
                   'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY',
                   'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
                   'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH',
                   'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'TERRITORIES',
                   'ALBERTA', 'BRITISH COLUMBIA', 'MANITOBA', 'NEW BRUNSWICK', 'NEWFOUNDLAND AND LABRADOR',
                   'NORTHWEST TERRITORIES', 'NOVA SCOTIA', 'ONTARIO', 'PRINCE EDWARD ISLAND', 'QUEBEC', 'SASKATCHEWAN',
                   'YUKON TERRITORY', 'AUSTRIA', 'BELGIUM', 'BULGARIA', 'CROATIA', 'CZECH REPUBLIC', 'DENMARK',
                   'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HUNGARY', 'ICELAND', 'IRELAND', 'ITALY', 'LUXEMBOURG',
                   'NETHERLANDS', 'NORWAY', 'POLAND', 'PORTUGAL', 'ROMANIA', 'RUSSIAN FEDERATION', 'SPAIN', 'SWEDEN',
                   'SWITZERLAND', 'TURKEY', 'UKRAINE', 'UNITED KINGDOM', 'BANGLADESH', 'CHINA', 'GUAM / MICRONESIA',
                   'HONG KONG', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'ISRAEL AND PALESTINE', 'JAPAN', 'KOREA',
                   'KUWAIT', 'LEBANON', 'MALAYSIA', 'PAKISTAN', 'PHILIPPINES', 'SINGAPORE', 'TAIWAN', 'THAILAND',
                   'UNITED ARAB EMIRATES', 'VIETNAM', 'AUSTRALIA', 'NEW ZEALAND', 'ARGENTINA', 'BOLIVIA', 'BRAZIL',
                   'CARIBBEAN ISLANDS', 'CHILE', 'COLOMBIA', 'COSTA RICA', 'DOMINICAN REPUBLIC', 'ECUADOR',
                   'EL SALVADOR', 'GUATEMALA', 'MEXICO', 'NICARAGUA', 'PANAMA', 'PERU', 'PUERTO RICO', 'URUGUAY',
                   'VENEZUELA', 'VIRGIN ISLANDS, U.S.', 'EGYPT', 'ETHIOPIA', 'GHANA', 'KENYA', 'MOROCCO',
                   'SOUTH AFRICA', 'TUNISIA']
    sub_headers_pos = [1, 11, 16, 25, 31, 60, 69, 74, 76, 78, 103, 115, 117, 122, 134, 145, 157, 166, 173, 182, 184,
                       191, 197, 216, 225, 232, 242, 251, 257, 261, 263, 268, 275, 296, 309, 314, 330, 336, 347, 363,
                       365, 372, 378, 387, 415, 421, 423, 435, 446, 455, 467, 469, 474, 482, 496, 498, 500, 502, 505,
                       507, 528, 530, 536, 539, 542, 544, 546, 548, 550, 552, 554, 556, 570, 586, 588, 590, 592, 594,
                       606, 608, 610, 612, 614, 618, 620, 623, 635, 637, 643, 645, 647, 676, 678, 691, 693, 695, 712,
                       714, 716, 718, 723, 732, 734, 736, 738, 740, 742, 752, 754, 756, 758, 760, 763, 776, 782, 784,
                       786, 796, 798, 800, 802, 804, 806, 808, 810, 812, 829, 831, 833, 835, 837, 839, 841, 844, 846,
                       848, 850, 852, 854, 859]
    headers_pos = [0, 473, 541, 675, 762, 781, 843]
    stuff_for_frontend = stuff_for_frontend = {
        'links': links, 'link_texts': link_texts, 'headers_pos': headers_pos, 'sub_headers_pos': sub_headers_pos,
        'headers':
            headers, 'sub_headers': sub_headers
    }
    return render(request, 'base.html', stuff_for_frontend)


def new_search(request):
    # links = ['', '', 'auburn.craigslist.org', 'bham.craigslist.org', 'dothan.craigslist.org', 'shoals.craigslist.org', 'gadsden.craigslist.org', 'huntsville.craigslist.org', 'mobile.craigslist.org', 'montgomery.craigslist.org', 'tuscaloosa.craigslist.org', '', 'anchorage.craigslist.org', 'fairbanks.craigslist.org', 'kenai.craigslist.org', 'juneau.craigslist.org', '', 'flagstaff.craigslist.org', 'mohave.craigslist.org', 'phoenix.craigslist.org', 'prescott.craigslist.org', 'showlow.craigslist.org', 'sierravista.craigslist.org', 'tucson.craigslist.org', 'yuma.craigslist.org', '', 'fayar.craigslist.org', 'fortsmith.craigslist.org', 'jonesboro.craigslist.org', 'littlerock.craigslist.org', 'texarkana.craigslist.org', '', 'bakersfield.craigslist.org', 'chico.craigslist.org', 'fresno.craigslist.org', 'goldcountry.craigslist.org', 'hanford.craigslist.org', 'humboldt.craigslist.org', 'imperial.craigslist.org', 'inlandempire.craigslist.org', 'losangeles.craigslist.org', 'mendocino.craigslist.org', 'merced.craigslist.org', 'modesto.craigslist.org', 'monterey.craigslist.org', 'orangecounty.craigslist.org', 'palmsprings.craigslist.org', 'redding.craigslist.org', 'sacramento.craigslist.org', 'sandiego.craigslist.org', 'sfbay.craigslist.org', 'slo.craigslist.org', 'santabarbara.craigslist.org', 'santamaria.craigslist.org', 'siskiyou.craigslist.org', 'stockton.craigslist.org', 'susanville.craigslist.org', 'ventura.craigslist.org', 'visalia.craigslist.org', 'yubasutter.craigslist.org', '', 'boulder.craigslist.org', 'cosprings.craigslist.org', 'denver.craigslist.org', 'eastco.craigslist.org', 'fortcollins.craigslist.org', 'rockies.craigslist.org', 'pueblo.craigslist.org', 'westslope.craigslist.org', '', 'newlondon.craigslist.org', 'hartford.craigslist.org', 'newhaven.craigslist.org', 'nwct.craigslist.org', '', 'delaware.craigslist.org', '', 'washingtondc.craigslist.org', '', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fbrw', 'daytona.craigslist.org', 'keys.craigslist.org', 'fortlauderdale.craigslist.org', 'fortmyers.craigslist.org', 'gainesville.craigslist.org', 'cfl.craigslist.org', 'jacksonville.craigslist.org', 'lakeland.craigslist.org', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc', 'lakecity.craigslist.org', 'ocala.craigslist.org', 'okaloosa.craigslist.org', 'orlando.craigslist.org', 'panamacity.craigslist.org', 'pensacola.craigslist.org', 'sarasota.craigslist.org', 'miami.craigslist.org', 'spacecoast.craigslist.org', 'staugustine.craigslist.org', 'tallahassee.craigslist.org', 'tampa.craigslist.org', 'treasure.craigslist.org', '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc', '', 'albanyga.craigslist.org', 'athensga.craigslist.org', 'atlanta.craigslist.org', 'augusta.craigslist.org', 'brunswick.craigslist.org', 'columbusga.craigslist.org', 'macon.craigslist.org', 'nwga.craigslist.org', 'savannah.craigslist.org', 'statesboro.craigslist.org', 'valdosta.craigslist.org', '', 'honolulu.craigslist.org', '', 'boise.craigslist.org', 'eastidaho.craigslist.org', 'lewiston.craigslist.org', 'twinfalls.craigslist.org', '', 'bn.craigslist.org', 'chambana.craigslist.org', 'chicago.craigslist.org', 'decatur.craigslist.org', 'lasalle.craigslist.org', 'mattoon.craigslist.org', 'peoria.craigslist.org', 'rockford.craigslist.org', 'carbondale.craigslist.org', 'springfieldil.craigslist.org', 'quincy.craigslist.org', '', 'bloomington.craigslist.org', 'evansville.craigslist.org', 'fortwayne.craigslist.org', 'indianapolis.craigslist.org', 'kokomo.craigslist.org', 'tippecanoe.craigslist.org', 'muncie.craigslist.org', 'richmondin.craigslist.org', 'southbend.craigslist.org', 'terrehaute.craigslist.org', '', 'ames.craigslist.org', 'cedarrapids.craigslist.org', 'desmoines.craigslist.org', 'dubuque.craigslist.org', 'fortdodge.craigslist.org', 'iowacity.craigslist.org', 'masoncity.craigslist.org', 'quadcities.craigslist.org', 'siouxcity.craigslist.org', 'ottumwa.craigslist.org', 'waterloo.craigslist.org', '', 'lawrence.craigslist.org', 'ksu.craigslist.org', 'nwks.craigslist.org', 'salina.craigslist.org', 'seks.craigslist.org', 'swks.craigslist.org', 'topeka.craigslist.org', 'wichita.craigslist.org', '', 'bgky.craigslist.org', 'eastky.craigslist.org', 'lexington.craigslist.org', 'louisville.craigslist.org', 'owensboro.craigslist.org', 'westky.craigslist.org', '', 'batonrouge.craigslist.org', 'cenla.craigslist.org', 'houma.craigslist.org', 'lafayette.craigslist.org', 'lakecharles.craigslist.org', 'monroe.craigslist.org', 'neworleans.craigslist.org', 'shreveport.craigslist.org', '', 'maine.craigslist.org', '', 'annapolis.craigslist.org', 'baltimore.craigslist.org', 'easternshore.craigslist.org', 'frederick.craigslist.org', 'smd.craigslist.org', 'westmd.craigslist.org', '', 'boston.craigslist.org', 'capecod.craigslist.org', 'southcoast.craigslist.org', 'westernmass.craigslist.org', 'worcester.craigslist.org', '', 'annarbor.craigslist.org', 'battlecreek.craigslist.org', 'centralmich.craigslist.org', 'detroit.craigslist.org', 'flint.craigslist.org', 'grandrapids.craigslist.org', 'holland.craigslist.org', 'jxn.craigslist.org', 'kalamazoo.craigslist.org', 'lansing.craigslist.org', 'monroemi.craigslist.org', 'muskegon.craigslist.org', 'nmi.craigslist.org', 'porthuron.craigslist.org', 'saginaw.craigslist.org', 'swmi.craigslist.org', 'thumb.craigslist.org', 'up.craigslist.org', '', 'bemidji.craigslist.org', 'brainerd.craigslist.org', 'duluth.craigslist.org', 'mankato.craigslist.org', 'minneapolis.craigslist.org', 'rmn.craigslist.org', 'marshall.craigslist.org', 'stcloud.craigslist.org', '', 'gulfport.craigslist.org', 'hattiesburg.craigslist.org', 'jackson.craigslist.org', 'meridian.craigslist.org', 'northmiss.craigslist.org', 'natchez.craigslist.org', '', 'columbiamo.craigslist.org', 'joplin.craigslist.org', 'kansascity.craigslist.org', 'kirksville.craigslist.org', 'loz.craigslist.org', 'semo.craigslist.org', 'springfield.craigslist.org', 'stjoseph.craigslist.org', 'stlouis.craigslist.org', '', 'billings.craigslist.org', 'bozeman.craigslist.org', 'butte.craigslist.org', 'greatfalls.craigslist.org', 'helena.craigslist.org', 'kalispell.craigslist.org', 'missoula.craigslist.org', 'montana.craigslist.org', '', 'grandisland.craigslist.org', 'lincoln.craigslist.org', 'northplatte.craigslist.org', 'omaha.craigslist.org', 'scottsbluff.craigslist.org', '', 'elko.craigslist.org', 'lasvegas.craigslist.org', 'reno.craigslist.org', '', 'nh.craigslist.org', '', 'cnj.craigslist.org', 'jerseyshore.craigslist.org', 'newjersey.craigslist.org', 'southjersey.craigslist.org', '', 'albuquerque.craigslist.org', 'clovis.craigslist.org', 'farmington.craigslist.org', 'lascruces.craigslist.org', 'roswell.craigslist.org', 'santafe.craigslist.org', '', 'albany.craigslist.org', 'binghamton.craigslist.org', 'buffalo.craigslist.org', 'catskills.craigslist.org', 'chautauqua.craigslist.org', 'elmira.craigslist.org', 'fingerlakes.craigslist.org', 'glensfalls.craigslist.org', 'hudsonvalley.craigslist.org', 'ithaca.craigslist.org', 'longisland.craigslist.org', 'newyork.craigslist.org', 'oneonta.craigslist.org', 'plattsburgh.craigslist.org', 'potsdam.craigslist.org', 'rochester.craigslist.org', 'syracuse.craigslist.org', 'twintiers.craigslist.org', 'utica.craigslist.org', 'watertown.craigslist.org', '', 'asheville.craigslist.org', 'boone.craigslist.org', 'charlotte.craigslist.org', 'eastnc.craigslist.org', 'fayetteville.craigslist.org', 'greensboro.craigslist.org', 'hickory.craigslist.org', 'onslow.craigslist.org', 'outerbanks.craigslist.org', 'raleigh.craigslist.org', 'wilmington.craigslist.org', 'winstonsalem.craigslist.org', '', 'bismarck.craigslist.org', 'fargo.craigslist.org', 'grandforks.craigslist.org', 'nd.craigslist.org', '', 'akroncanton.craigslist.org', 'ashtabula.craigslist.org', 'athensohio.craigslist.org', 'chillicothe.craigslist.org', 'cincinnati.craigslist.org', 'cleveland.craigslist.org', 'columbus.craigslist.org', 'dayton.craigslist.org', 'limaohio.craigslist.org', 'mansfield.craigslist.org', 'sandusky.craigslist.org', 'toledo.craigslist.org', 'tuscarawas.craigslist.org', 'youngstown.craigslist.org', 'zanesville.craigslist.org', '', 'lawton.craigslist.org', 'enid.craigslist.org', 'oklahomacity.craigslist.org', 'stillwater.craigslist.org', 'tulsa.craigslist.org', '', 'bend.craigslist.org', 'corvallis.craigslist.org', 'eastoregon.craigslist.org', 'eugene.craigslist.org', 'klamath.craigslist.org', 'medford.craigslist.org', 'oregoncoast.craigslist.org', 'portland.craigslist.org', 'roseburg.craigslist.org', 'salem.craigslist.org', '', 'altoona.craigslist.org', 'chambersburg.craigslist.org', 'erie.craigslist.org', 'harrisburg.craigslist.org', 'lancaster.craigslist.org', 'allentown.craigslist.org', 'meadville.craigslist.org', 'philadelphia.craigslist.org', 'pittsburgh.craigslist.org', 'poconos.craigslist.org', 'reading.craigslist.org', 'scranton.craigslist.org', 'pennstate.craigslist.org', 'williamsport.craigslist.org', 'york.craigslist.org', '', 'providence.craigslist.org', '', 'charleston.craigslist.org', 'columbia.craigslist.org', 'florencesc.craigslist.org', 'greenville.craigslist.org', 'hiltonhead.craigslist.org', 'myrtlebeach.craigslist.org', '', 'nesd.craigslist.org', 'csd.craigslist.org', 'rapidcity.craigslist.org', 'siouxfalls.craigslist.org', 'sd.craigslist.org', '', 'chattanooga.craigslist.org', 'clarksville.craigslist.org', 'cookeville.craigslist.org', 'jacksontn.craigslist.org', 'knoxville.craigslist.org', 'memphis.craigslist.org', 'nashville.craigslist.org', 'tricities.craigslist.org', '', 'abilene.craigslist.org', 'amarillo.craigslist.org', 'austin.craigslist.org', 'beaumont.craigslist.org', 'brownsville.craigslist.org', 'collegestation.craigslist.org', 'corpuschristi.craigslist.org', 'dallas.craigslist.org', 'nacogdoches.craigslist.org', 'delrio.craigslist.org', 'elpaso.craigslist.org', 'galveston.craigslist.org', 'houston.craigslist.org', 'killeen.craigslist.org', 'laredo.craigslist.org', 'lubbock.craigslist.org', 'mcallen.craigslist.org', 'odessa.craigslist.org', 'sanangelo.craigslist.org', 'sanantonio.craigslist.org', 'sanmarcos.craigslist.org', 'bigbend.craigslist.org', 'texoma.craigslist.org', 'easttexas.craigslist.org', 'victoriatx.craigslist.org', 'waco.craigslist.org', 'wichitafalls.craigslist.org', '', 'logan.craigslist.org', 'ogden.craigslist.org', 'provo.craigslist.org', 'saltlakecity.craigslist.org', 'stgeorge.craigslist.org', '', 'vermont.craigslist.org', '', 'charlottesville.craigslist.org', 'danville.craigslist.org', 'fredericksburg.craigslist.org', 'norfolk.craigslist.org', 'harrisonburg.craigslist.org', 'lynchburg.craigslist.org', 'blacksburg.craigslist.org', 'richmond.craigslist.org', 'roanoke.craigslist.org', 'swva.craigslist.org', 'winchester.craigslist.org', '', 'bellingham.craigslist.org', 'kpr.craigslist.org', 'moseslake.craigslist.org', 'olympic.craigslist.org', 'pullman.craigslist.org', 'seattle.craigslist.org', 'skagit.craigslist.org', 'spokane.craigslist.org', 'wenatchee.craigslist.org', 'yakima.craigslist.org', '', 'charlestonwv.craigslist.org', 'martinsburg.craigslist.org', 'huntington.craigslist.org', 'morgantown.craigslist.org', 'wheeling.craigslist.org', 'parkersburg.craigslist.org', 'swv.craigslist.org', 'wv.craigslist.org', '', 'appleton.craigslist.org', 'eauclaire.craigslist.org', 'greenbay.craigslist.org', 'janesville.craigslist.org', 'racine.craigslist.org', 'lacrosse.craigslist.org', 'madison.craigslist.org', 'milwaukee.craigslist.org', 'northernwi.craigslist.org', 'sheboygan.craigslist.org', 'wausau.craigslist.org', '', 'wyoming.craigslist.org', '', 'micronesia.craigslist.org', 'puertorico.craigslist.org', 'virgin.craigslist.org', 'calgary.craigslist.org', '', 'edmonton.craigslist.org', 'ftmcmurray.craigslist.org', 'lethbridge.craigslist.org', 'hat.craigslist.org', 'peace.craigslist.org', 'reddeer.craigslist.org', 'cariboo.craigslist.org', '', 'comoxvalley.craigslist.org', 'abbotsford.craigslist.org', 'kamloops.craigslist.org', 'kelowna.craigslist.org', 'kootenays.craigslist.org', 'nanaimo.craigslist.org', 'princegeorge.craigslist.org', 'skeena.craigslist.org', 'sunshine.craigslist.org', 'vancouver.craigslist.org', 'victoria.craigslist.org', 'whistler.craigslist.org', 'winnipeg.craigslist.org', '', 'newbrunswick.craigslist.org', '', 'newfoundland.craigslist.org', '', 'territories.craigslist.org', '', 'yellowknife.craigslist.org', 'halifax.craigslist.org', '', 'barrie.craigslist.org', '', 'belleville.craigslist.org', 'brantford.craigslist.org', 'chatham.craigslist.org', 'cornwall.craigslist.org', 'guelph.craigslist.org', 'hamilton.craigslist.org', 'kingston.craigslist.org', 'kitchener.craigslist.org', 'londonon.craigslist.org', 'niagara.craigslist.org', 'ottawa.craigslist.org', 'owensound.craigslist.org', 'peterborough.craigslist.org', 'sarnia.craigslist.org', 'soo.craigslist.org', 'sudbury.craigslist.org', 'thunderbay.craigslist.org', 'toronto.craigslist.org', 'windsor.craigslist.org', 'pei.craigslist.org', '', 'montreal.craigslist.org', '', 'quebec.craigslist.org', 'saguenay.craigslist.org', 'sherbrooke.craigslist.org', 'troisrivieres.craigslist.org', '', '', 'regina.craigslist.org', 'saskatoon.craigslist.org', '', 'whitehorse.craigslist.org', 'vienna.craigslist.at', '', 'brussels.craigslist.org', '', 'bulgaria.craigslist.org', '', 'zagreb.craigslist.org', '', 'prague.craigslist.cz', '', 'copenhagen.craigslist.org', '', 'helsinki.craigslist.fi', '', 'bordeaux.craigslist.org', '', 'rennes.craigslist.org', 'grenoble.craigslist.org', 'lille.craigslist.org', 'loire.craigslist.org', 'lyon.craigslist.org', 'marseilles.craigslist.org', 'montpellier.craigslist.org', 'cotedazur.craigslist.org', 'rouen.craigslist.org', 'paris.craigslist.org', 'strasbourg.craigslist.org', 'toulouse.craigslist.org', 'berlin.craigslist.de', '', 'bremen.craigslist.de', 'cologne.craigslist.de', 'dresden.craigslist.de', 'dusseldorf.craigslist.de', 'essen.craigslist.de', 'frankfurt.craigslist.de', 'hamburg.craigslist.de', 'hannover.craigslist.de', 'heidelberg.craigslist.de', 'kaiserslautern.craigslist.de', 'leipzig.craigslist.de', 'munich.craigslist.de', 'nuremberg.craigslist.de', 'stuttgart.craigslist.de', 'athens.craigslist.gr', '', 'budapest.craigslist.org', '', 'reykjavik.craigslist.org', '', 'dublin.craigslist.org', '', 'bologna.craigslist.it', '', 'florence.craigslist.it', 'genoa.craigslist.it', 'milan.craigslist.it', 'naples.craigslist.it', 'perugia.craigslist.it', 'rome.craigslist.it', 'sardinia.craigslist.it', 'sicily.craigslist.it', 'torino.craigslist.it', 'venice.craigslist.it', 'luxembourg.craigslist.org', '', 'amsterdam.craigslist.org', '', 'oslo.craigslist.org', '', 'warsaw.craigslist.pl', '', 'faro.craigslist.pt', '', 'lisbon.craigslist.pt', 'porto.craigslist.pt', 'bucharest.craigslist.org', '', 'moscow.craigslist.org', '', 'stpetersburg.craigslist.org', 'alicante.craigslist.es', '', 'baleares.craigslist.es', 'barcelona.craigslist.es', 'bilbao.craigslist.es', '', 'cadiz.craigslist.es', 'canarias.craigslist.es', 'granada.craigslist.es', 'madrid.craigslist.es', 'malaga.craigslist.es', 'sevilla.craigslist.es', 'valencia.craigslist.es', '', 'stockholm.craigslist.se', '', 'basel.craigslist.ch', 'bern.craigslist.ch', 'geneva.craigslist.ch', 'lausanne.craigslist.ch', 'zurich.craigslist.ch', '', 'istanbul.craigslist.com.tr', '', 'ukraine.craigslist.org', '', 'aberdeen.craigslist.co.uk', 'bath.craigslist.co.uk', 'belfast.craigslist.co.uk', 'birmingham.craigslist.co.uk', 'brighton.craigslist.co.uk', 'bristol.craigslist.co.uk', 'cambridge.craigslist.co.uk', 'cardiff.craigslist.co.uk', 'coventry.craigslist.co.uk', 'derby.craigslist.co.uk', 'devon.craigslist.co.uk', 'dundee.craigslist.co.uk', 'norwich.craigslist.co.uk', 'eastmids.craigslist.co.uk', 'edinburgh.craigslist.co.uk', 'essex.craigslist.co.uk', 'glasgow.craigslist.co.uk', 'hampshire.craigslist.co.uk', 'kent.craigslist.co.uk', 'leeds.craigslist.co.uk', 'liverpool.craigslist.co.uk', 'london.craigslist.co.uk', 'manchester.craigslist.co.uk', 'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk', 'oxford.craigslist.co.uk', 'sheffield.craigslist.co.uk', 'bangladesh.craigslist.org', '', 'beijing.craigslist.com.cn', '', 'chengdu.craigslist.com.cn', 'chongqing.craigslist.com.cn', 'dalian.craigslist.com.cn', 'guangzhou.craigslist.com.cn', 'hangzhou.craigslist.com.cn', 'nanjing.craigslist.com.cn', 'shanghai.craigslist.com.cn', 'shenyang.craigslist.com.cn', 'shenzhen.craigslist.com.cn', 'wuhan.craigslist.com.cn', 'xian.craigslist.com.cn', 'micronesia.craigslist.org', '', 'hongkong.craigslist.hk', '', 'ahmedabad.craigslist.co.in', '', 'bangalore.craigslist.co.in', 'bhubaneswar.craigslist.co.in', 'chandigarh.craigslist.co.in', 'chennai.craigslist.co.in', 'delhi.craigslist.co.in', 'goa.craigslist.co.in', 'hyderabad.craigslist.co.in', 'indore.craigslist.co.in', 'jaipur.craigslist.co.in', 'kerala.craigslist.co.in', 'kolkata.craigslist.co.in', 'lucknow.craigslist.co.in', 'mumbai.craigslist.co.in', 'pune.craigslist.co.in', 'surat.craigslist.co.in', 'jakarta.craigslist.org', '', 'tehran.craigslist.org', '', 'baghdad.craigslist.org', '', 'haifa.craigslist.org', '', 'jerusalem.craigslist.org', 'telaviv.craigslist.org', 'ramallah.craigslist.org', 'fukuoka.craigslist.jp', '', 'hiroshima.craigslist.jp', 'nagoya.craigslist.jp', 'okinawa.craigslist.jp', 'osaka.craigslist.jp', 'sapporo.craigslist.jp', 'sendai.craigslist.jp', 'tokyo.craigslist.jp', 'seoul.craigslist.co.kr', '', 'kuwait.craigslist.org', '', 'beirut.craigslist.org', '', 'malaysia.craigslist.org', '', 'pakistan.craigslist.org', '', 'bacolod.craigslist.com.ph', '', 'naga.craigslist.com.ph', 'cdo.craigslist.com.ph', 'cebu.craigslist.com.ph', 'davaocity.craigslist.com.ph', 'iloilo.craigslist.com.ph', 'manila.craigslist.com.ph', 'pampanga.craigslist.com.ph', 'zamboanga.craigslist.com.ph', 'singapore.craigslist.com.sg', '', 'taipei.craigslist.com.tw', '', 'bangkok.craigslist.co.th', '', 'dubai.craigslist.org', '', 'vietnam.craigslist.org', '', 'adelaide.craigslist.com.au', 'brisbane.craigslist.com.au', '', 'cairns.craigslist.com.au', 'canberra.craigslist.com.au', 'darwin.craigslist.com.au', 'goldcoast.craigslist.com.au', 'melbourne.craigslist.com.au', 'ntl.craigslist.com.au', 'perth.craigslist.com.au', 'sydney.craigslist.com.au', 'hobart.craigslist.com.au', 'wollongong.craigslist.com.au', 'auckland.craigslist.org', 'christchurch.craigslist.org', '', 'dunedin.craigslist.co.nz', 'wellington.craigslist.org', 'buenosaires.craigslist.org', 'lapaz.craigslist.org', 'belohorizonte.craigslist.org', '', 'brasilia.craigslist.org', '', 'curitiba.craigslist.org', '', 'fortaleza.craigslist.org', 'portoalegre.craigslist.org', 'recife.craigslist.org', 'rio.craigslist.org', 'salvador.craigslist.org', '', 'saopaulo.craigslist.org', 'caribbean.craigslist.org', 'santiago.craigslist.org', '', 'colombia.craigslist.org', '', 'costarica.craigslist.org', '', 'santodomingo.craigslist.org', '', 'quito.craigslist.org', '', 'elsalvador.craigslist.org', '', 'guatemala.craigslist.org', '', 'acapulco.craigslist.com.mx', '', 'bajasur.craigslist.com.mx', '', 'chihuahua.craigslist.com.mx', 'juarez.craigslist.com.mx', 'guadalajara.craigslist.com.mx', 'guanajuato.craigslist.com.mx', 'hermosillo.craigslist.com.mx', 'mazatlan.craigslist.com.mx', 'mexicocity.craigslist.com.mx', 'monterrey.craigslist.com.mx', 'oaxaca.craigslist.com.mx', 'puebla.craigslist.com.mx', 'pv.craigslist.com.mx', 'tijuana.craigslist.com.mx', 'veracruz.craigslist.com.mx', 'yucatan.craigslist.com.mx', 'managua.craigslist.org', 'panama.craigslist.org', '', 'lima.craigslist.org', '', 'puertorico.craigslist.org', '', 'montevideo.craigslist.org', '', 'caracas.craigslist.org', '', 'virgin.craigslist.org', '', 'cairo.craigslist.org', '', 'addisababa.craigslist.org', 'accra.craigslist.org', '', 'kenya.craigslist.org', '', 'casablanca.craigslist.org', '', 'capetown.craigslist.co.za', '', 'durban.craigslist.co.za', '', 'johannesburg.craigslist.co.za', '', 'pretoria.craigslist.co.za', 'tunis.craigslist.org', '', '', '', '']
    links = ['auburn.craigslist.org', 'bham.craigslist.org', 'dothan.craigslist.org', 'shoals.craigslist.org',
             'gadsden.craigslist.org', 'huntsville.craigslist.org', 'mobile.craigslist.org',
             'montgomery.craigslist.org',
             'tuscaloosa.craigslist.org', 'anchorage.craigslist.org', 'fairbanks.craigslist.org',
             'kenai.craigslist.org',
             'juneau.craigslist.org', 'flagstaff.craigslist.org', 'mohave.craigslist.org', 'phoenix.craigslist.org',
             'prescott.craigslist.org', 'showlow.craigslist.org', 'sierravista.craigslist.org', 'tucson.craigslist.org',
             'yuma.craigslist.org', 'fayar.craigslist.org', 'fortsmith.craigslist.org', 'jonesboro.craigslist.org',
             'littlerock.craigslist.org', 'texarkana.craigslist.org', 'bakersfield.craigslist.org',
             'chico.craigslist.org',
             'fresno.craigslist.org', 'goldcountry.craigslist.org', 'hanford.craigslist.org', 'humboldt.craigslist.org',
             'imperial.craigslist.org', 'inlandempire.craigslist.org', 'losangeles.craigslist.org',
             'mendocino.craigslist.org', 'merced.craigslist.org', 'modesto.craigslist.org', 'monterey.craigslist.org',
             'orangecounty.craigslist.org', 'palmsprings.craigslist.org', 'redding.craigslist.org',
             'sacramento.craigslist.org', 'sandiego.craigslist.org', 'sfbay.craigslist.org', 'slo.craigslist.org',
             'santabarbara.craigslist.org', 'santamaria.craigslist.org', 'siskiyou.craigslist.org',
             'stockton.craigslist.org', 'susanville.craigslist.org', 'ventura.craigslist.org', 'visalia.craigslist.org',
             'yubasutter.craigslist.org', 'boulder.craigslist.org', 'cosprings.craigslist.org', 'denver.craigslist.org',
             'eastco.craigslist.org', 'fortcollins.craigslist.org', 'rockies.craigslist.org', 'pueblo.craigslist.org',
             'westslope.craigslist.org', 'newlondon.craigslist.org', 'hartford.craigslist.org',
             'newhaven.craigslist.org',
             'nwct.craigslist.org', 'delaware.craigslist.org', 'washingtondc.craigslist.org',
             '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fbrw', 'daytona.craigslist.org', 'keys.craigslist.org',
             'fortlauderdale.craigslist.org', 'fortmyers.craigslist.org', 'gainesville.craigslist.org',
             'cfl.craigslist.org', 'jacksonville.craigslist.org', 'lakeland.craigslist.org',
             '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fmdc', 'lakecity.craigslist.org', 'ocala.craigslist.org',
             'okaloosa.craigslist.org', 'orlando.craigslist.org', 'panamacity.craigslist.org',
             'pensacola.craigslist.org',
             'sarasota.craigslist.org', 'miami.craigslist.org', 'spacecoast.craigslist.org',
             'staugustine.craigslist.org',
             'tallahassee.craigslist.org', 'tampa.craigslist.org', 'treasure.craigslist.org',
             '/go.php?u=http%3A%2F%2Fmiami.craigslist.org%2Fpbc', 'albanyga.craigslist.org', 'athensga.craigslist.org',
             'atlanta.craigslist.org', 'augusta.craigslist.org', 'brunswick.craigslist.org',
             'columbusga.craigslist.org',
             'macon.craigslist.org', 'nwga.craigslist.org', 'savannah.craigslist.org', 'statesboro.craigslist.org',
             'valdosta.craigslist.org', 'honolulu.craigslist.org', 'boise.craigslist.org', 'eastidaho.craigslist.org',
             'lewiston.craigslist.org', 'twinfalls.craigslist.org', 'bn.craigslist.org', 'chambana.craigslist.org',
             'chicago.craigslist.org', 'decatur.craigslist.org', 'lasalle.craigslist.org', 'mattoon.craigslist.org',
             'peoria.craigslist.org', 'rockford.craigslist.org', 'carbondale.craigslist.org',
             'springfieldil.craigslist.org', 'quincy.craigslist.org', 'bloomington.craigslist.org',
             'evansville.craigslist.org', 'fortwayne.craigslist.org', 'indianapolis.craigslist.org',
             'kokomo.craigslist.org', 'tippecanoe.craigslist.org', 'muncie.craigslist.org', 'richmondin.craigslist.org',
             'southbend.craigslist.org', 'terrehaute.craigslist.org', 'ames.craigslist.org',
             'cedarrapids.craigslist.org',
             'desmoines.craigslist.org', 'dubuque.craigslist.org', 'fortdodge.craigslist.org',
             'iowacity.craigslist.org',
             'masoncity.craigslist.org', 'quadcities.craigslist.org', 'siouxcity.craigslist.org',
             'ottumwa.craigslist.org',
             'waterloo.craigslist.org', 'lawrence.craigslist.org', 'ksu.craigslist.org', 'nwks.craigslist.org',
             'salina.craigslist.org', 'seks.craigslist.org', 'swks.craigslist.org', 'topeka.craigslist.org',
             'wichita.craigslist.org', 'bgky.craigslist.org', 'eastky.craigslist.org', 'lexington.craigslist.org',
             'louisville.craigslist.org', 'owensboro.craigslist.org', 'westky.craigslist.org',
             'batonrouge.craigslist.org',
             'cenla.craigslist.org', 'houma.craigslist.org', 'lafayette.craigslist.org', 'lakecharles.craigslist.org',
             'monroe.craigslist.org', 'neworleans.craigslist.org', 'shreveport.craigslist.org', 'maine.craigslist.org',
             'annapolis.craigslist.org', 'baltimore.craigslist.org', 'easternshore.craigslist.org',
             'frederick.craigslist.org', 'smd.craigslist.org', 'westmd.craigslist.org', 'boston.craigslist.org',
             'capecod.craigslist.org', 'southcoast.craigslist.org', 'westernmass.craigslist.org',
             'worcester.craigslist.org', 'annarbor.craigslist.org', 'battlecreek.craigslist.org',
             'centralmich.craigslist.org', 'detroit.craigslist.org', 'flint.craigslist.org',
             'grandrapids.craigslist.org',
             'holland.craigslist.org', 'jxn.craigslist.org', 'kalamazoo.craigslist.org', 'lansing.craigslist.org',
             'monroemi.craigslist.org', 'muskegon.craigslist.org', 'nmi.craigslist.org', 'porthuron.craigslist.org',
             'saginaw.craigslist.org', 'swmi.craigslist.org', 'thumb.craigslist.org', 'up.craigslist.org',
             'bemidji.craigslist.org', 'brainerd.craigslist.org', 'duluth.craigslist.org', 'mankato.craigslist.org',
             'minneapolis.craigslist.org', 'rmn.craigslist.org', 'marshall.craigslist.org', 'stcloud.craigslist.org',
             'gulfport.craigslist.org', 'hattiesburg.craigslist.org', 'jackson.craigslist.org',
             'meridian.craigslist.org',
             'northmiss.craigslist.org', 'natchez.craigslist.org', 'columbiamo.craigslist.org', 'joplin.craigslist.org',
             'kansascity.craigslist.org', 'kirksville.craigslist.org', 'loz.craigslist.org', 'semo.craigslist.org',
             'springfield.craigslist.org', 'stjoseph.craigslist.org', 'stlouis.craigslist.org',
             'billings.craigslist.org',
             'bozeman.craigslist.org', 'butte.craigslist.org', 'greatfalls.craigslist.org', 'helena.craigslist.org',
             'kalispell.craigslist.org', 'missoula.craigslist.org', 'montana.craigslist.org',
             'grandisland.craigslist.org',
             'lincoln.craigslist.org', 'northplatte.craigslist.org', 'omaha.craigslist.org',
             'scottsbluff.craigslist.org',
             'elko.craigslist.org', 'lasvegas.craigslist.org', 'reno.craigslist.org', 'nh.craigslist.org',
             'cnj.craigslist.org', 'jerseyshore.craigslist.org', 'newjersey.craigslist.org',
             'southjersey.craigslist.org',
             'albuquerque.craigslist.org', 'clovis.craigslist.org', 'farmington.craigslist.org',
             'lascruces.craigslist.org',
             'roswell.craigslist.org', 'santafe.craigslist.org', 'albany.craigslist.org', 'binghamton.craigslist.org',
             'buffalo.craigslist.org', 'catskills.craigslist.org', 'chautauqua.craigslist.org', 'elmira.craigslist.org',
             'fingerlakes.craigslist.org', 'glensfalls.craigslist.org', 'hudsonvalley.craigslist.org',
             'ithaca.craigslist.org', 'longisland.craigslist.org', 'newyork.craigslist.org', 'oneonta.craigslist.org',
             'plattsburgh.craigslist.org', 'potsdam.craigslist.org', 'rochester.craigslist.org',
             'syracuse.craigslist.org',
             'twintiers.craigslist.org', 'utica.craigslist.org', 'watertown.craigslist.org', 'asheville.craigslist.org',
             'boone.craigslist.org', 'charlotte.craigslist.org', 'eastnc.craigslist.org', 'fayetteville.craigslist.org',
             'greensboro.craigslist.org', 'hickory.craigslist.org', 'onslow.craigslist.org',
             'outerbanks.craigslist.org',
             'raleigh.craigslist.org', 'wilmington.craigslist.org', 'winstonsalem.craigslist.org',
             'bismarck.craigslist.org', 'fargo.craigslist.org', 'grandforks.craigslist.org', 'nd.craigslist.org',
             'akroncanton.craigslist.org', 'ashtabula.craigslist.org', 'athensohio.craigslist.org',
             'chillicothe.craigslist.org', 'cincinnati.craigslist.org', 'cleveland.craigslist.org',
             'columbus.craigslist.org', 'dayton.craigslist.org', 'limaohio.craigslist.org', 'mansfield.craigslist.org',
             'sandusky.craigslist.org', 'toledo.craigslist.org', 'tuscarawas.craigslist.org',
             'youngstown.craigslist.org',
             'zanesville.craigslist.org', 'lawton.craigslist.org', 'enid.craigslist.org', 'oklahomacity.craigslist.org',
             'stillwater.craigslist.org', 'tulsa.craigslist.org', 'bend.craigslist.org', 'corvallis.craigslist.org',
             'eastoregon.craigslist.org', 'eugene.craigslist.org', 'klamath.craigslist.org', 'medford.craigslist.org',
             'oregoncoast.craigslist.org', 'portland.craigslist.org', 'roseburg.craigslist.org', 'salem.craigslist.org',
             'altoona.craigslist.org', 'chambersburg.craigslist.org', 'erie.craigslist.org',
             'harrisburg.craigslist.org',
             'lancaster.craigslist.org', 'allentown.craigslist.org', 'meadville.craigslist.org',
             'philadelphia.craigslist.org', 'pittsburgh.craigslist.org', 'poconos.craigslist.org',
             'reading.craigslist.org',
             'scranton.craigslist.org', 'pennstate.craigslist.org', 'williamsport.craigslist.org',
             'york.craigslist.org',
             'providence.craigslist.org', 'charleston.craigslist.org', 'columbia.craigslist.org',
             'florencesc.craigslist.org', 'greenville.craigslist.org', 'hiltonhead.craigslist.org',
             'myrtlebeach.craigslist.org', 'nesd.craigslist.org', 'csd.craigslist.org', 'rapidcity.craigslist.org',
             'siouxfalls.craigslist.org', 'sd.craigslist.org', 'chattanooga.craigslist.org',
             'clarksville.craigslist.org',
             'cookeville.craigslist.org', 'jacksontn.craigslist.org', 'knoxville.craigslist.org',
             'memphis.craigslist.org',
             'nashville.craigslist.org', 'tricities.craigslist.org', 'abilene.craigslist.org',
             'amarillo.craigslist.org',
             'austin.craigslist.org', 'beaumont.craigslist.org', 'brownsville.craigslist.org',
             'collegestation.craigslist.org', 'corpuschristi.craigslist.org', 'dallas.craigslist.org',
             'nacogdoches.craigslist.org', 'delrio.craigslist.org', 'elpaso.craigslist.org', 'galveston.craigslist.org',
             'houston.craigslist.org', 'killeen.craigslist.org', 'laredo.craigslist.org', 'lubbock.craigslist.org',
             'mcallen.craigslist.org', 'odessa.craigslist.org', 'sanangelo.craigslist.org', 'sanantonio.craigslist.org',
             'sanmarcos.craigslist.org', 'bigbend.craigslist.org', 'texoma.craigslist.org', 'easttexas.craigslist.org',
             'victoriatx.craigslist.org', 'waco.craigslist.org', 'wichitafalls.craigslist.org', 'logan.craigslist.org',
             'ogden.craigslist.org', 'provo.craigslist.org', 'saltlakecity.craigslist.org', 'stgeorge.craigslist.org',
             'vermont.craigslist.org', 'charlottesville.craigslist.org', 'danville.craigslist.org',
             'fredericksburg.craigslist.org', 'norfolk.craigslist.org', 'harrisonburg.craigslist.org',
             'lynchburg.craigslist.org', 'blacksburg.craigslist.org', 'richmond.craigslist.org',
             'roanoke.craigslist.org',
             'swva.craigslist.org', 'winchester.craigslist.org', 'bellingham.craigslist.org', 'kpr.craigslist.org',
             'moseslake.craigslist.org', 'olympic.craigslist.org', 'pullman.craigslist.org', 'seattle.craigslist.org',
             'skagit.craigslist.org', 'spokane.craigslist.org', 'wenatchee.craigslist.org', 'yakima.craigslist.org',
             'charlestonwv.craigslist.org', 'martinsburg.craigslist.org', 'huntington.craigslist.org',
             'morgantown.craigslist.org', 'wheeling.craigslist.org', 'parkersburg.craigslist.org', 'swv.craigslist.org',
             'wv.craigslist.org', 'appleton.craigslist.org', 'eauclaire.craigslist.org', 'greenbay.craigslist.org',
             'janesville.craigslist.org', 'racine.craigslist.org', 'lacrosse.craigslist.org', 'madison.craigslist.org',
             'milwaukee.craigslist.org', 'northernwi.craigslist.org', 'sheboygan.craigslist.org',
             'wausau.craigslist.org',
             'wyoming.craigslist.org', 'micronesia.craigslist.org', 'puertorico.craigslist.org',
             'virgin.craigslist.org',
             'calgary.craigslist.org', 'edmonton.craigslist.org', 'ftmcmurray.craigslist.org',
             'lethbridge.craigslist.org',
             'hat.craigslist.org', 'peace.craigslist.org', 'reddeer.craigslist.org', 'cariboo.craigslist.org',
             'comoxvalley.craigslist.org', 'abbotsford.craigslist.org', 'kamloops.craigslist.org',
             'kelowna.craigslist.org',
             'kootenays.craigslist.org', 'nanaimo.craigslist.org', 'princegeorge.craigslist.org',
             'skeena.craigslist.org',
             'sunshine.craigslist.org', 'vancouver.craigslist.org', 'victoria.craigslist.org',
             'whistler.craigslist.org',
             'winnipeg.craigslist.org', 'newbrunswick.craigslist.org', 'newfoundland.craigslist.org',
             'territories.craigslist.org', 'yellowknife.craigslist.org', 'halifax.craigslist.org',
             'barrie.craigslist.org',
             'belleville.craigslist.org', 'brantford.craigslist.org', 'chatham.craigslist.org',
             'cornwall.craigslist.org',
             'guelph.craigslist.org', 'hamilton.craigslist.org', 'kingston.craigslist.org', 'kitchener.craigslist.org',
             'londonon.craigslist.org', 'niagara.craigslist.org', 'ottawa.craigslist.org', 'owensound.craigslist.org',
             'peterborough.craigslist.org', 'sarnia.craigslist.org', 'soo.craigslist.org', 'sudbury.craigslist.org',
             'thunderbay.craigslist.org', 'toronto.craigslist.org', 'windsor.craigslist.org', 'pei.craigslist.org',
             'montreal.craigslist.org', 'quebec.craigslist.org', 'saguenay.craigslist.org', 'sherbrooke.craigslist.org',
             'troisrivieres.craigslist.org', 'regina.craigslist.org', 'saskatoon.craigslist.org',
             'whitehorse.craigslist.org', 'vienna.craigslist.at', 'brussels.craigslist.org', 'bulgaria.craigslist.org',
             'zagreb.craigslist.org', 'prague.craigslist.cz', 'copenhagen.craigslist.org', 'helsinki.craigslist.fi',
             'bordeaux.craigslist.org', 'rennes.craigslist.org', 'grenoble.craigslist.org', 'lille.craigslist.org',
             'loire.craigslist.org', 'lyon.craigslist.org', 'marseilles.craigslist.org', 'montpellier.craigslist.org',
             'cotedazur.craigslist.org', 'rouen.craigslist.org', 'paris.craigslist.org', 'strasbourg.craigslist.org',
             'toulouse.craigslist.org', 'berlin.craigslist.de', 'bremen.craigslist.de', 'cologne.craigslist.de',
             'dresden.craigslist.de', 'dusseldorf.craigslist.de', 'essen.craigslist.de', 'frankfurt.craigslist.de',
             'hamburg.craigslist.de', 'hannover.craigslist.de', 'heidelberg.craigslist.de',
             'kaiserslautern.craigslist.de',
             'leipzig.craigslist.de', 'munich.craigslist.de', 'nuremberg.craigslist.de', 'stuttgart.craigslist.de',
             'athens.craigslist.gr', 'budapest.craigslist.org', 'reykjavik.craigslist.org', 'dublin.craigslist.org',
             'bologna.craigslist.it', 'florence.craigslist.it', 'genoa.craigslist.it', 'milan.craigslist.it',
             'naples.craigslist.it', 'perugia.craigslist.it', 'rome.craigslist.it', 'sardinia.craigslist.it',
             'sicily.craigslist.it', 'torino.craigslist.it', 'venice.craigslist.it', 'luxembourg.craigslist.org',
             'amsterdam.craigslist.org', 'oslo.craigslist.org', 'warsaw.craigslist.pl', 'faro.craigslist.pt',
             'lisbon.craigslist.pt', 'porto.craigslist.pt', 'bucharest.craigslist.org', 'moscow.craigslist.org',
             'stpetersburg.craigslist.org', 'alicante.craigslist.es', 'baleares.craigslist.es',
             'barcelona.craigslist.es',
             'bilbao.craigslist.es', 'cadiz.craigslist.es', 'canarias.craigslist.es', 'granada.craigslist.es',
             'madrid.craigslist.es', 'malaga.craigslist.es', 'sevilla.craigslist.es', 'valencia.craigslist.es',
             'stockholm.craigslist.se', 'basel.craigslist.ch', 'bern.craigslist.ch', 'geneva.craigslist.ch',
             'lausanne.craigslist.ch', 'zurich.craigslist.ch', 'istanbul.craigslist.com.tr', 'ukraine.craigslist.org',
             'aberdeen.craigslist.co.uk', 'bath.craigslist.co.uk', 'belfast.craigslist.co.uk',
             'birmingham.craigslist.co.uk', 'brighton.craigslist.co.uk', 'bristol.craigslist.co.uk',
             'cambridge.craigslist.co.uk', 'cardiff.craigslist.co.uk', 'coventry.craigslist.co.uk',
             'derby.craigslist.co.uk', 'devon.craigslist.co.uk', 'dundee.craigslist.co.uk', 'norwich.craigslist.co.uk',
             'eastmids.craigslist.co.uk', 'edinburgh.craigslist.co.uk', 'essex.craigslist.co.uk',
             'glasgow.craigslist.co.uk', 'hampshire.craigslist.co.uk', 'kent.craigslist.co.uk',
             'leeds.craigslist.co.uk',
             'liverpool.craigslist.co.uk', 'london.craigslist.co.uk', 'manchester.craigslist.co.uk',
             'newcastle.craigslist.co.uk', 'nottingham.craigslist.co.uk', 'oxford.craigslist.co.uk',
             'sheffield.craigslist.co.uk', 'bangladesh.craigslist.org', 'beijing.craigslist.com.cn',
             'chengdu.craigslist.com.cn', 'chongqing.craigslist.com.cn', 'dalian.craigslist.com.cn',
             'guangzhou.craigslist.com.cn', 'hangzhou.craigslist.com.cn', 'nanjing.craigslist.com.cn',
             'shanghai.craigslist.com.cn', 'shenyang.craigslist.com.cn', 'shenzhen.craigslist.com.cn',
             'wuhan.craigslist.com.cn', 'xian.craigslist.com.cn', 'micronesia.craigslist.org', 'hongkong.craigslist.hk',
             'ahmedabad.craigslist.co.in', 'bangalore.craigslist.co.in', 'bhubaneswar.craigslist.co.in',
             'chandigarh.craigslist.co.in', 'chennai.craigslist.co.in', 'delhi.craigslist.co.in',
             'goa.craigslist.co.in',
             'hyderabad.craigslist.co.in', 'indore.craigslist.co.in', 'jaipur.craigslist.co.in',
             'kerala.craigslist.co.in',
             'kolkata.craigslist.co.in', 'lucknow.craigslist.co.in', 'mumbai.craigslist.co.in', 'pune.craigslist.co.in',
             'surat.craigslist.co.in', 'jakarta.craigslist.org', 'tehran.craigslist.org', 'baghdad.craigslist.org',
             'haifa.craigslist.org', 'jerusalem.craigslist.org', 'telaviv.craigslist.org', 'ramallah.craigslist.org',
             'fukuoka.craigslist.jp', 'hiroshima.craigslist.jp', 'nagoya.craigslist.jp', 'okinawa.craigslist.jp',
             'osaka.craigslist.jp', 'sapporo.craigslist.jp', 'sendai.craigslist.jp', 'tokyo.craigslist.jp',
             'seoul.craigslist.co.kr', 'kuwait.craigslist.org', 'beirut.craigslist.org', 'malaysia.craigslist.org',
             'pakistan.craigslist.org', 'bacolod.craigslist.com.ph', 'naga.craigslist.com.ph', 'cdo.craigslist.com.ph',
             'cebu.craigslist.com.ph', 'davaocity.craigslist.com.ph', 'iloilo.craigslist.com.ph',
             'manila.craigslist.com.ph', 'pampanga.craigslist.com.ph', 'zamboanga.craigslist.com.ph',
             'singapore.craigslist.com.sg', 'taipei.craigslist.com.tw', 'bangkok.craigslist.co.th',
             'dubai.craigslist.org',
             'vietnam.craigslist.org', 'adelaide.craigslist.com.au', 'brisbane.craigslist.com.au',
             'cairns.craigslist.com.au', 'canberra.craigslist.com.au', 'darwin.craigslist.com.au',
             'goldcoast.craigslist.com.au', 'melbourne.craigslist.com.au', 'ntl.craigslist.com.au',
             'perth.craigslist.com.au', 'sydney.craigslist.com.au', 'hobart.craigslist.com.au',
             'wollongong.craigslist.com.au', 'auckland.craigslist.org', 'christchurch.craigslist.org',
             'dunedin.craigslist.co.nz', 'wellington.craigslist.org', 'buenosaires.craigslist.org',
             'lapaz.craigslist.org',
             'belohorizonte.craigslist.org', 'brasilia.craigslist.org', 'curitiba.craigslist.org',
             'fortaleza.craigslist.org', 'portoalegre.craigslist.org', 'recife.craigslist.org', 'rio.craigslist.org',
             'salvador.craigslist.org', 'saopaulo.craigslist.org', 'caribbean.craigslist.org',
             'santiago.craigslist.org',
             'colombia.craigslist.org', 'costarica.craigslist.org', 'santodomingo.craigslist.org',
             'quito.craigslist.org',
             'elsalvador.craigslist.org', 'guatemala.craigslist.org', 'acapulco.craigslist.com.mx',
             'bajasur.craigslist.com.mx', 'chihuahua.craigslist.com.mx', 'juarez.craigslist.com.mx',
             'guadalajara.craigslist.com.mx', 'guanajuato.craigslist.com.mx', 'hermosillo.craigslist.com.mx',
             'mazatlan.craigslist.com.mx', 'mexicocity.craigslist.com.mx', 'monterrey.craigslist.com.mx',
             'oaxaca.craigslist.com.mx', 'puebla.craigslist.com.mx', 'pv.craigslist.com.mx',
             'tijuana.craigslist.com.mx',
             'veracruz.craigslist.com.mx', 'yucatan.craigslist.com.mx', 'managua.craigslist.org',
             'panama.craigslist.org',
             'lima.craigslist.org', 'puertorico.craigslist.org', 'montevideo.craigslist.org', 'caracas.craigslist.org',
             'virgin.craigslist.org', 'cairo.craigslist.org', 'addisababa.craigslist.org', 'accra.craigslist.org',
             'kenya.craigslist.org', 'casablanca.craigslist.org', 'capetown.craigslist.co.za',
             'durban.craigslist.co.za',
             'johannesburg.craigslist.co.za', 'pretoria.craigslist.co.za', 'tunis.craigslist.org']
    link_texts = ['US', 'ALABAMA', 'Auburn', 'Birmingham', 'Dothan', 'Florence / Muscle Shoals', 'Gadsden-Anniston',
                  'Huntsville / Decatur', 'Mobile', 'Montgomery', 'Tuscaloosa', 'ALASKA', 'Anchorage / Mat-Su',
                  'Fairbanks', 'Kenai Peninsula', 'Southeast Alaska', 'ARIZONA', 'Flagstaff / Sedona', 'Mohave County',
                  'Phoenix', 'Prescott', 'Show Low', 'Sierra Vista', 'Tucson', 'Yuma', 'ARKANSAS', 'Fayetteville ',
                  'Fort Smith', 'Jonesboro', 'Little Rock', 'Texarkana', 'CALIFORNIA', 'Bakersfield', 'Chico',
                  'Fresno / Madera', 'Gold Country', 'Hanford-Corcoran', 'Humboldt County', 'Imperial County',
                  'Inland Empire', 'Los Angeles', 'Mendocino County', 'Merced', 'Modesto', 'Monterey Bay',
                  'Orange County', 'Palm Springs', 'Redding', 'Sacramento', 'San Diego', 'San Francisco Bay Area',
                  'San Luis Obispo', 'Santa Barbara', 'Santa Maria', 'Siskiyou County', 'Stockton', 'Susanville',
                  'Ventura County', 'Visalia-Tulare', 'Yuba-Sutter', 'COLORADO', 'Boulder', 'Colorado Springs',
                  'Denver', 'Eastern CO', 'Fort Collins / North CO', 'High Rockies', 'Pueblo', 'Western Slope',
                  'CONNECTICUT', 'Eastern CT', 'Hartford', 'New Haven', 'Northwest Ct', 'DELAWARE', 'Delaware',
                  'DISTRICT OF COLUMBIA', 'Washington', 'FLORIDA', 'Broward County', 'Daytona Beach', 'Florida Keys',
                  'Fort Lauderdale', 'Ft Myers / Sw Florida', 'Gainesville', 'Heartland Florida', 'Jacksonville',
                  'Lakeland', 'Miami / Dade', 'North Central FL', 'Ocala', 'Okaloosa / Walton', 'Orlando',
                  'Panama City', 'Pensacola', 'Sarasota-Bradenton', 'South Florida', 'Space Coast', 'St Augustine',
                  'Tallahassee', 'Tampa Bay Area', 'Treasure Coast', 'Palm Beach County', 'GEORGIA', 'Albany ',
                  'Athens', 'Atlanta', 'Augusta', 'Brunswick', 'Columbus ', 'Macon / Warner Robins', 'Northwest GA',
                  'Savannah / Hinesville', 'Statesboro', 'Valdosta', 'HAWAII', 'Hawaii', 'IDAHO', 'Boise', 'East Idaho',
                  'Lewiston / Clarkston', 'Twin Falls', 'ILLINOIS', 'Bloomington-Normal', 'Champaign Urbana', 'Chicago',
                  'Decatur', 'La Salle Co', 'Mattoon-Charleston', 'Peoria', 'Rockford', 'Southern Illinois',
                  'Springfield ', 'Western IL', 'INDIANA', 'Bloomington', 'Evansville', 'Fort Wayne', 'Indianapolis',
                  'Kokomo', 'Lafayette / West Lafayette', 'Muncie / Anderson', 'Richmond ', 'South Bend / Michiana',
                  'Terre Haute', 'IOWA', 'Ames', 'Cedar Rapids', 'Des Moines', 'Dubuque', 'Fort Dodge', 'Iowa City',
                  'Mason City', 'Quad Cities', 'Sioux City', 'Southeast IA', 'Waterloo / Cedar Falls', 'KANSAS',
                  'Lawrence', 'Manhattan', 'Northwest KS', 'Salina', 'Southeast KS', 'Southwest KS', 'Topeka',
                  'Wichita', 'KENTUCKY', 'Bowling Green', 'Eastern Kentucky', 'Lexington', 'Louisville', 'Owensboro',
                  'Western KY', 'LOUISIANA', 'Baton Rouge', 'Central Louisiana', 'Houma', 'Lafayette', 'Lake Charles',
                  'Monroe', 'New Orleans', 'Shreveport', 'MAINE', 'Maine', 'MARYLAND', 'Annapolis', 'Baltimore',
                  'Eastern Shore', 'Frederick', 'Southern Maryland', 'Western Maryland', 'MASSACHUSETTS', 'Boston',
                  'Cape Cod / Islands', 'South Coast', 'Western Massachusetts', 'Worcester / Central MA', 'MICHIGAN',
                  'Ann Arbor', 'Battle Creek', 'Central Michigan', 'Detroit Metro', 'Flint', 'Grand Rapids', 'Holland',
                  'Jackson ', 'Kalamazoo', 'Lansing', 'Monroe ', 'Muskegon', 'Northern Michigan', 'Port Huron',
                  'Saginaw-Midland-Baycity', 'Southwest Michigan', 'The Thumb', 'Upper Peninsula', 'MINNESOTA',
                  'Bemidji', 'Brainerd', 'Duluth / Superior', 'Mankato', 'Minneapolis / St Paul', 'Rochester ',
                  'Southwest MN', 'St Cloud', 'MISSISSIPPI', 'Gulfport / Biloxi', 'Hattiesburg', 'Jackson', 'Meridian',
                  'North Mississippi', 'Southwest MS', 'MISSOURI', 'Columbia / Jeff City', 'Joplin', 'Kansas City',
                  'Kirksville', 'Lake Of The Ozarks', 'Southeast Missouri', 'Springfield', 'St Joseph', 'St Louis',
                  'MONTANA', 'Billings', 'Bozeman', 'Butte', 'Great Falls', 'Helena', 'Kalispell', 'Missoula',
                  'Eastern Montana', 'NEBRASKA', 'Grand Island', 'Lincoln', 'North Platte', 'Omaha / Council Bluffs',
                  'Scottsbluff / Panhandle', 'NEVADA', 'Elko', 'Las Vegas', 'Reno / Tahoe', 'NEW HAMPSHIRE',
                  'New Hampshire', 'NEW JERSEY', 'Central NJ', 'Jersey Shore', 'North Jersey', 'South Jersey',
                  'NEW MEXICO', 'Albuquerque', 'Clovis / Portales', 'Farmington', 'Las Cruces', 'Roswell / Carlsbad',
                  'Santa Fe / Taos', 'NEW YORK', 'Albany', 'Binghamton', 'Buffalo', 'Catskills', 'Chautauqua',
                  'Elmira-Corning', 'Finger Lakes', 'Glens Falls', 'Hudson Valley', 'Ithaca', 'Long Island',
                  'New York City', 'Oneonta', 'Plattsburgh-Adirondacks', 'Potsdam-Canton-Massena', 'Rochester',
                  'Syracuse', 'Twin Tiers NY/PA', 'Utica-Rome-Oneida', 'Watertown', 'NORTH CAROLINA', 'Asheville',
                  'Boone', 'Charlotte', 'Eastern Nc', 'Fayetteville', 'Greensboro', 'Hickory / Lenoir', 'Jacksonville ',
                  'Outer Banks', 'Raleigh / Durham / CH', 'Wilmington', 'Winston-Salem', 'NORTH DAKOTA', 'Bismarck',
                  'Fargo / Moorhead', 'Grand Forks', 'North Dakota', 'OHIO', 'Akron / Canton', 'Ashtabula', 'Athens ',
                  'Chillicothe', 'Cincinnati', 'Cleveland', 'Columbus', 'Dayton / Springfield', 'Lima / Findlay',
                  'Mansfield', 'Sandusky', 'Toledo', 'Tuscarawas Co', 'Youngstown', 'Zanesville / Cambridge',
                  'OKLAHOMA', 'Lawton', 'Northwest OK', 'Oklahoma City', 'Stillwater', 'Tulsa', 'OREGON', 'Bend',
                  'Corvallis/Albany', 'East Oregon', 'Eugene', 'Klamath Falls', 'Medford-Ashland', 'Oregon Coast',
                  'Portland', 'Roseburg', 'Salem', 'PENNSYLVANIA', 'Altoona-Johnstown', 'Cumberland Valley', 'Erie',
                  'Harrisburg', 'Lancaster', 'Lehigh Valley', 'Meadville', 'Philadelphia', 'Pittsburgh', 'Poconos',
                  'Reading', 'Scranton / Wilkes-Barre', 'State College', 'Williamsport', 'York', 'RHODE ISLAND',
                  'Rhode Island', 'SOUTH CAROLINA', 'Charleston', 'Columbia', 'Florence', 'Greenville / Upstate',
                  'Hilton Head', 'Myrtle Beach', 'SOUTH DAKOTA', 'Northeast SD', 'Pierre / Central SD',
                  'Rapid City / West SD', 'Sioux Falls / Se SD', 'South Dakota', 'TENNESSEE', 'Chattanooga',
                  'Clarksville', 'Cookeville', 'Jackson  ', 'Knoxville', 'Memphis', 'Nashville', 'Tri-Cities', 'TEXAS',
                  'Abilene', 'Amarillo', 'Austin', 'Beaumont / Port Arthur', 'Brownsville', 'College Station',
                  'Corpus Christi', 'Dallas / Fort Worth', 'Deep East Texas', 'Del Rio / Eagle Pass', 'El Paso',
                  'Galveston', 'Houston', 'Killeen / Temple / Ft Hood', 'Laredo', 'Lubbock', 'Mcallen / Edinburg',
                  'Odessa / Midland', 'San Angelo', 'San Antonio', 'San Marcos', 'Southwest TX', 'Texoma',
                  'Tyler / East TX', 'Victoria ', 'Waco', 'Wichita Falls', 'UTAH', 'Logan', 'Ogden-Clearfield',
                  'Provo / Orem', 'Salt Lake City', 'St George', 'VERMONT', 'Vermont', 'VIRGINIA', 'Charlottesville',
                  'Danville', 'Fredericksburg', 'Hampton Roads', 'Harrisonburg', 'Lynchburg', 'New River Valley',
                  'Richmond', 'Roanoke', 'Southwest VA', 'Winchester', 'WASHINGTON', 'Bellingham',
                  'Kennewick-Pasco-Richland', 'Moses Lake', 'Olympic Peninsula', 'Pullman / Moscow', 'Seattle-Tacoma',
                  'Skagit / Island / SJI', "Spokane / Coeur D'Alene", 'Wenatchee', 'Yakima', 'WEST VIRGINIA',
                  'Charleston ', 'Eastern Panhandle', 'Huntington-Ashland', 'Morgantown', 'Northern Panhandle',
                  'Parkersburg-Marietta', 'Southern WV', 'West Virginia (Old)', 'WISCONSIN', 'Appleton-Oshkosh-FDL',
                  'Eau Claire', 'Green Bay', 'Janesville', 'Kenosha-Racine', 'La Crosse', 'Madison', 'Milwaukee',
                  'Northern Wi', 'Sheboygan', 'Wausau', 'WYOMING', 'Wyoming', 'TERRITORIES', 'Guam-Micronesia',
                  'Puerto Rico', 'U.S. Virgin Islands', 'CANADA', 'ALBERTA', 'Calgary', 'Edmonton', 'Ft Mcmurray',
                  'Lethbridge', 'Medicine Hat', 'Peace River Country', 'Red Deer', 'BRITISH COLUMBIA', 'Cariboo',
                  'Comox Valley', 'Fraser Valley', 'Kamloops', 'Kelowna / Okanagan', 'Kootenays', 'Nanaimo',
                  'Prince George', 'Skeena-Bulkley', 'Sunshine Coast', 'Vancouver', 'Victoria', 'Whistler', 'MANITOBA',
                  'Winnipeg', 'NEW BRUNSWICK', 'New Brunswick', 'NEWFOUNDLAND AND LABRADOR', "St John'S",
                  'NORTHWEST TERRITORIES', 'Territories', 'Yellowknife', 'NOVA SCOTIA', 'Halifax', 'ONTARIO', 'Barrie',
                  'Belleville', 'Brantford-Woodstock', 'Chatham-Kent', 'Cornwall', 'Guelph', 'Hamilton-Burlington',
                  'Kingston', 'Kitchener-Waterloo-Cambridge', 'London ', 'Niagara Region', 'Ottawa-Hull-Gatineau',
                  'Owen Sound', 'Peterborough', 'Sarnia', 'Sault Ste Marie', 'Sudbury', 'Thunder Bay', 'Toronto',
                  'Windsor', 'PRINCE EDWARD ISLAND', 'Prince Edward Island', 'QUEBEC', 'Montreal', 'Quebec City',
                  'Saguenay', 'Sherbrooke', 'Trois-Rivieres', 'SASKATCHEWAN', 'Regina', 'Saskatoon', 'YUKON TERRITORY',
                  'Whitehorse', 'EUROPE', 'AUSTRIA', 'Vienna', 'BELGIUM', 'Belgium', 'BULGARIA', 'Bulgaria', 'CROATIA',
                  'Croatia', 'CZECH REPUBLIC', 'Prague', 'DENMARK', 'Copenhagen', 'FINLAND', 'Finland', 'FRANCE',
                  'Bordeaux', 'Brittany', 'Grenoble', 'Lille', 'Loire Valley', 'Lyon', 'Marseille', 'Montpellier',
                  "Nice / Cote D'Azur", 'Normandy', 'Paris', 'Strasbourg', 'Toulouse', 'GERMANY', 'Berlin', 'Bremen',
                  'Cologne', 'Dresden', 'Dusseldorf', 'Essen / Ruhr', 'Frankfurt', 'Hamburg', 'Hannover', 'Heidelberg',
                  'Kaiserslautern', 'Leipzig', 'Munich', 'Nuremberg', 'Stuttgart', 'GREECE', 'Greece', 'HUNGARY',
                  'Budapest', 'ICELAND', 'Reykjavik', 'IRELAND', 'Dublin', 'ITALY', 'Bologna', 'Florence / Tuscany',
                  'Genoa', 'Milan', 'Napoli / Campania', 'Perugia', 'Rome', 'Sardinia', 'Sicilia', 'Torino',
                  'Venice / Veneto', 'LUXEMBOURG', 'Luxembourg', 'NETHERLANDS', 'Amsterdam / Randstad', 'NORWAY',
                  'Norway', 'POLAND', 'Poland', 'PORTUGAL', 'Faro / Algarve', 'Lisbon', 'Porto', 'ROMANIA', 'Romania',
                  'RUSSIAN FEDERATION', 'Moscow', 'St Petersburg', 'SPAIN', 'Alicante', 'Baleares', 'Barcelona',
                  'Bilbao', 'Cadiz', 'Canarias', 'Granada', 'Madrid', 'Malaga', 'Sevilla', 'Valencia', 'SWEDEN',
                  'Sweden', 'SWITZERLAND', 'Basel', 'Bern', 'Geneva', 'Lausanne', 'Zurich', 'TURKEY', 'Turkey',
                  'UKRAINE', 'Ukraine', 'UNITED KINGDOM', 'Aberdeen', 'Bath', 'Belfast', 'Birmingham / West Mids',
                  'Brighton', 'Bristol', 'Cambridge, UK', 'Cardiff / Wales', 'Coventry', 'Derby', 'Devon & Cornwall',
                  'Dundee', 'East Anglia', 'East Midlands', 'Edinburgh', 'Essex', 'Glasgow', 'Hampshire', 'Kent',
                  'Leeds', 'Liverpool', 'London', 'Manchester', 'Newcastle / NE England', 'Nottingham', 'Oxford',
                  'Sheffield', 'ASIA, PACIFIC AND MIDDLE EAST', 'BANGLADESH', 'Bangladesh', 'CHINA', 'Beijing',
                  'Chengdu', 'Chongqing', 'Dalian', 'Guangzhou', 'Hangzhou', 'Nanjing', 'Shanghai', 'Shenyang',
                  'Shenzhen', 'Wuhan', "Xi'An", 'GUAM / MICRONESIA', 'Guam-Micronesia', 'HONG KONG', 'Hong Kong',
                  'INDIA', 'Ahmedabad', 'Bangalore', 'Bhubaneswar', 'Chandigarh', 'Chennai (Madras)', 'Delhi', 'Goa',
                  'Hyderabad', 'Indore', 'Jaipur', 'Kerala', 'Kolkata (Calcutta)', 'Lucknow', 'Mumbai', 'Pune',
                  'Surat Surat', 'INDONESIA', 'Indonesia', 'IRAN', 'Iran', 'IRAQ', 'Iraq', 'ISRAEL AND PALESTINE',
                  'Haifa', 'Jerusalem', 'Tel Aviv', 'West Bank', 'JAPAN', 'Fukuoka', 'Hiroshima', 'Nagoya', 'Okinawa',
                  'Osaka-Kobe-Kyoto', 'Sapporo', 'Sendai', 'Tokyo', 'KOREA', 'Seoul', 'KUWAIT', 'Kuwait', 'LEBANON',
                  'Beirut, Lebanon', 'MALAYSIA', 'Malaysia', 'PAKISTAN', 'Pakistan', 'PHILIPPINES', 'Bacolod',
                  'Bicol Region', 'Cagayan De Oro', 'Cebu', 'Davao City', 'Iloilo', 'Manila', 'Pampanga', 'Zamboanga',
                  'SINGAPORE', 'Singapore', 'TAIWAN', 'Taiwan', 'THAILAND', 'Thailand', 'UNITED ARAB EMIRATES',
                  'United Arab Emirates', 'VIETNAM', 'Vietnam', 'OCEANIA', 'AUSTRALIA', 'Adelaide', 'Brisbane',
                  'Cairns', 'Canberra', 'Darwin', 'Gold Coast', 'Melbourne', 'Newcastle, NSW', 'Perth', 'Sydney',
                  'Tasmania', 'Wollongong', 'NEW ZEALAND', 'Auckland', 'Christchurch', 'Dunedin', 'Wellington',
                  'LATIN AMERICA AND CARIBBEAN', 'ARGENTINA', 'Buenos Aires', 'BOLIVIA', 'Bolivia', 'BRAZIL',
                  'Belo Horizonte', 'Brasilia', 'Curitiba', 'Fortaleza', 'Porto Alegre', 'Recife', 'Rio De Janeiro',
                  'Salvador, Bahia', 'Sao Paulo', 'CARIBBEAN ISLANDS', 'Caribbean Islands', 'CHILE', 'Chile',
                  'COLOMBIA', 'Colombia', 'COSTA RICA', 'Costa Rica', 'DOMINICAN REPUBLIC', 'Dominican Republic',
                  'ECUADOR', 'Ecuador', 'EL SALVADOR', 'El Salvador', 'GUATEMALA', 'Guatemala', 'MEXICO', 'Acapulco',
                  'Baja California Sur', 'Chihuahua', 'Ciudad Juarez', 'Guadalajara', 'Guanajuato', 'Hermosillo',
                  'Mazatlan', 'Mexico City', 'Monterrey', 'Oaxaca', 'Puebla', 'Puerto Vallarta', 'Tijuana', 'Veracruz',
                  'Yucatan', 'NICARAGUA', 'Nicaragua', 'PANAMA', 'Panama', 'PERU', 'Peru', 'PUERTO RICO', 'Puerto Rico',
                  'URUGUAY', 'Montevideo', 'VENEZUELA', 'Venezuela', 'VIRGIN ISLANDS, U.S.', 'Virgin Islands', 'AFRICA',
                  'EGYPT', 'Egypt', 'ETHIOPIA', 'Ethiopia', 'GHANA', 'Ghana', 'KENYA', 'Kenya', 'MOROCCO', 'Morocco',
                  'SOUTH AFRICA', 'Cape Town', 'Durban', 'Johannesburg', 'Pretoria', 'TUNISIA', 'Tunisia']
    headers = ['US', 'CANADA', 'EUROPE', 'ASIA, PACIFIC AND MIDDLE EAST', 'OCEANIA', 'LATIN AMERICA AND CARIBBEAN',
               'AFRICA']
    sub_headers = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE',
                   'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA',
                   'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
                   'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY',
                   'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
                   'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH',
                   'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'TERRITORIES',
                   'ALBERTA', 'BRITISH COLUMBIA', 'MANITOBA', 'NEW BRUNSWICK', 'NEWFOUNDLAND AND LABRADOR',
                   'NORTHWEST TERRITORIES', 'NOVA SCOTIA', 'ONTARIO', 'PRINCE EDWARD ISLAND', 'QUEBEC', 'SASKATCHEWAN',
                   'YUKON TERRITORY', 'AUSTRIA', 'BELGIUM', 'BULGARIA', 'CROATIA', 'CZECH REPUBLIC', 'DENMARK',
                   'FINLAND', 'FRANCE', 'GERMANY', 'GREECE', 'HUNGARY', 'ICELAND', 'IRELAND', 'ITALY', 'LUXEMBOURG',
                   'NETHERLANDS', 'NORWAY', 'POLAND', 'PORTUGAL', 'ROMANIA', 'RUSSIAN FEDERATION', 'SPAIN', 'SWEDEN',
                   'SWITZERLAND', 'TURKEY', 'UKRAINE', 'UNITED KINGDOM', 'BANGLADESH', 'CHINA', 'GUAM / MICRONESIA',
                   'HONG KONG', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'ISRAEL AND PALESTINE', 'JAPAN', 'KOREA',
                   'KUWAIT', 'LEBANON', 'MALAYSIA', 'PAKISTAN', 'PHILIPPINES', 'SINGAPORE', 'TAIWAN', 'THAILAND',
                   'UNITED ARAB EMIRATES', 'VIETNAM', 'AUSTRALIA', 'NEW ZEALAND', 'ARGENTINA', 'BOLIVIA', 'BRAZIL',
                   'CARIBBEAN ISLANDS', 'CHILE', 'COLOMBIA', 'COSTA RICA', 'DOMINICAN REPUBLIC', 'ECUADOR',
                   'EL SALVADOR', 'GUATEMALA', 'MEXICO', 'NICARAGUA', 'PANAMA', 'PERU', 'PUERTO RICO', 'URUGUAY',
                   'VENEZUELA', 'VIRGIN ISLANDS, U.S.', 'EGYPT', 'ETHIOPIA', 'GHANA', 'KENYA', 'MOROCCO',
                   'SOUTH AFRICA', 'TUNISIA']
    sub_headers_pos = [1, 11, 16, 25, 31, 60, 69, 74, 76, 78, 103, 115, 117, 122, 134, 145, 157, 166, 173, 182, 184,
                       191, 197, 216, 225, 232, 242, 251, 257, 261, 263, 268, 275, 296, 309, 314, 330, 336, 347, 363,
                       365, 372, 378, 387, 415, 421, 423, 435, 446, 455, 467, 469, 474, 482, 496, 498, 500, 502, 505,
                       507, 528, 530, 536, 539, 542, 544, 546, 548, 550, 552, 554, 556, 570, 586, 588, 590, 592, 594,
                       606, 608, 610, 612, 614, 618, 620, 623, 635, 637, 643, 645, 647, 676, 678, 691, 693, 695, 712,
                       714, 716, 718, 723, 732, 734, 736, 738, 740, 742, 752, 754, 756, 758, 760, 763, 776, 782, 784,
                       786, 796, 798, 800, 802, 804, 806, 808, 810, 812, 829, 831, 833, 835, 837, 839, 841, 844, 846,
                       848, 850, 852, 854, 859]
    headers_pos = [0, 473, 541, 675, 762, 781, 843]

    var = request.build_absolute_uri()
    print(var)
    search = request.POST.get('search')
    sort_abb = request.POST.get('sort')
    section_abb = request.POST.get('sections')
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')
    location = request.POST.get('location')
    min_bedroom = request.POST.get('min-bedroom-filter')
    max_bedroom = request.POST.get('max-bedroom-filter')
    min_bathroom = request.POST.get('min-bathroom-filter')
    max_bathroom = request.POST.get('max-bathroom-filter')
    models.Search.objects.create(search=search)
    print(quote_plus(search), sort_abb, section_abb, min_price, max_price, location, min_bedroom, max_bedroom,
          min_bathroom, max_bathroom)
    # search = 'ping pong'
    location_pos = link_texts.index(location)
    link_texts_slice = link_texts[:location_pos + 1]
    count = 0
    for texts in link_texts_slice:
        if texts.isupper():
            count += 1
    link = links[location_pos - count]
    sections_dict = {'Community': 'ccc', 'Events': 'eee', 'For sale': 'sss', 'Gigs': 'ggg', 'Housing': 'hhh',
                     'Jobs': 'jjj', 'Resumes': 'rrr', 'Services': 'bbb'}
    section = ''
    for key, value in sections_dict.items():
        if section_abb == value:
            section = key.lower()
    if section == 'for sale':
        section = 'for-sale'
    # BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/hhh?query=apartment&sort=rel&min_price=2000&max_price=4000&min_bedrooms=2&max_bedrooms=4&min_bathrooms=2&max_bathrooms=5'
    # BASE_CRAIGSLIST_URL = 'https://{}/d/{}/search/{}?sort={}&query={}&purveyor-input=all&min_price={}&max_price={}'
    BASE_CRAIGSLIST_URL = 'https://{}/d/{}/search/{}?sort={}&query={}&min_price={}&max_price={}&min_bedrooms={}&max_bedrooms={}&min_bathrooms={}&max_bathrooms={}'
    formats = [link, section, section_abb, sort_abb, quote_plus(search), min_price, max_price, min_bedroom, max_bedroom,
               min_bathroom, max_bathroom]
    filters = {'&min_price={}': min_price, '&max_price={}': max_price, '&min_bedrooms={}': min_bedroom,
               '&max_bedrooms={}': max_bedroom, '&min_bathrooms={}': min_bathroom, '&max_bathrooms={}': max_bathroom}
    for frag, filt in filters.items():
        if filt == '' or filt == None:
            BASE_CRAIGSLIST_URL = BASE_CRAIGSLIST_URL.split(frag)
            BASE_CRAIGSLIST_URL = ''.join(BASE_CRAIGSLIST_URL)
            formats.remove(filt)
    pos = 0
    # for braces in range(BASE_CRAIGSLIST_URL.find('{}')):
    for formatting in formats:
        print(formats)
        replacement = formats[pos]
        print(replacement)
        BASE_CRAIGSLIST_URL = BASE_CRAIGSLIST_URL.replace('{}', replacement, 1)
        pos += 1
    final_url = BASE_CRAIGSLIST_URL

    # if max_price == '':
    #     if min_price != '':
    #         if min_price.isdigit:
    #             BASE_CRAIGSLIST_URL = 'https://{}/d/{}/search/{}?sort={}&query={}&purveyor-input=all&min_price={}'
    #             final_url = BASE_CRAIGSLIST_URL.format(link, section, section_abb, sort_abb, quote_plus(search), min_price)
    #
    # if min_price == '':
    #     if max_price != '':
    #         if max_price.isdigit:
    #             BASE_CRAIGSLIST_URL = 'https://{}/d/{}/search/{}?sort={}&query={}&purveyor-input=all&max_price={}'
    #             final_url = BASE_CRAIGSLIST_URL.format(link, section, section_abb, sort_abb, quote_plus(search), max_price)
    #
    # if max_price != '':
    #     if min_price != '':
    #         BASE_CRAIGSLIST_URL = 'https://{}/d/{}/search/{}?sort={}&query={}&purveyor-input=all&min_price={}&max_price={}'
    #         final_url = BASE_CRAIGSLIST_URL.format(link, section, section_abb, sort_abb, quote_plus(search), min_price, max_price)
    print(final_url)
    # CHANGE THE SECTION VALUE BECAUSE OF THE FOLLOWING LOOP
    if section == 'for-sale':
        section = 'for sale'
    front_end_detail = []
    sort = ''
    sort_dict = {'upcoming': 'UPCOMING', 'date': 'DATE (NEWEST FIRST)', 'rel': 'RELEVANCE',
                 'priceasc': 'PRICE (ASCENDING)', 'pricedsc': 'PRICE (DESCENDING)'}
    for key in sections_dict.keys():
        if section.capitalize() == key:
            front_end_detail.append(key.upper())
    for key, value in sort_dict.items():
        if sort_abb == key:
            sort = value
            front_end_detail.append(sort)
    print(front_end_detail)
    # FOR HIDE.ME PROXY SITE
    driver.get('https://hide.me/en/proxy')
    proxy_options_dropdown = driver.find_elements_by_class_name('proxy_option')
    try:
        hide_slideout = driver.find_element_by_class_name('Slideout-trigger')
        hide_slideout.click()
    except:
        pass
    proxy_options_dropdown[1].click()
    encrypt_url_checkbox = driver.find_element_by_name("encodeURL")
    encrypt_url_checkbox.click()
    search_box_input = driver.find_element_by_id("u")
    search_box_input.send_keys(final_url)
    # search_box_input.send_keys('https://losangeles.craigslist.org/d/for-sale/search/sss?query=ping%20pong&sort=rel')
    search_box_input.submit()

    soup = BeautifulSoup(driver.page_source, features='html.parser')
    error = False
    try:
        driver.find_element_by_class_name("alert alert-sm alert-warning")
        error = True

    except:
        pass
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []
    base_post_url = 'https://'
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_datetime = post.find('time').get('title')
        mod_post_url = post.find('a').get('href')
        post_url = mod_post_url.split('%2F')
        pu_frags_without_and_sign = post_url[len(post_url) - 1].split('&')
        post_url.pop()
        post_url.pop(0)
        post_url.pop(0)
        post_url.append(pu_frags_without_and_sign[0])
        for fragment in post_url:
            base_post_url = base_post_url + fragment + '/'

        post_url = list(base_post_url)
        post_url.pop()
        post_url = ''.join(post_url)

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        # p_image_urls = []
        if post.find(class_='result-image').get('data-ids'):
            # post_image_data_ids = post.find(class_='result-image').get('data-ids')
            # post_image_data_ids = post_image_data_ids.split(',')
            # for data_id in post_image_data_ids:
            #     post_image_data_ids[post_image_data_ids.index(data_id)] = data_id.split(':')[1]
            #     post_image_url = BASE_IMAGE_URL.format(post_image_data_ids)
            #     p_image_urls.append(post_image_url)

            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
        else:
            post_image_url = 'https://www.craigslist.org/images/peace.jpg'

        base_post_url = 'https://'
        final_postings.append((post_title, post_url, post_price, post_image_url, post_datetime))
    # driver.close()
    stuff_for_frontend = {
        'search': search, 'section': section, 'sort_abb': sort_abb, 'final_postings': final_postings,
        'front_end_detail': front_end_detail,
        'links': links, 'headers': headers, 'sub_headers': sub_headers, 'link_texts': link_texts,
        'headers_pos': headers_pos, 'sub_headers_pos': sub_headers_pos,
        'error': error
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)

    # Todo: Add a category search functionality \/
    # Todo: Add a sort_abb functionality (Relevance, Newest, Price) \/
    # Todo: Region selection \/
    # FixMe: Location-Link relationship (Egypt returned tunisia.org) \/
    # Todo: Make Text Field and Dropdowns required (They must be filled) \/
    # Todo: Page not found banner text + Displaying texts to show results are from other regions \
    # Todo: Multiple images on a card
    # FixMe: Post-datetimes disturb card-images look
# Nothing found for that search. (All words must match.)
# Zero local results found. Here are some from nearby areas. Checking 'include nearby areas' will expand your search.
