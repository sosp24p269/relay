// Copyright 2018 Ulf Adams
//
// The contents of this file may be used under the terms of the Apache License,
// Version 2.0.
//
//    (See accompanying file LICENSE-Apache or copy at
//     http://www.apache.org/licenses/LICENSE-2.0)
//
// Alternatively, the contents of this file may be used under the terms of
// the Boost Software License, Version 1.0.
//    (See accompanying file LICENSE-Boost or copy at
//     https://www.boost.org/LICENSE_1_0.txt)
//
// Unless required by applicable law or agreed to in writing, this software
// is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.
#ifndef RYU_D2S_FULL_TABLE_H
#define RYU_D2S_FULL_TABLE_H

// These tables are generated by PrintDoubleLookupTable.
#define DOUBLE_POW5_INV_BITCOUNT 125
#define DOUBLE_POW5_BITCOUNT 125

static const uint64_t DOUBLE_POW5_INV_SPLIT[292][2] = {
  {                    1u, 2305843009213693952u }, { 11068046444225730970u, 1844674407370955161u },
  {  5165088340638674453u, 1475739525896764129u }, {  7821419487252849886u, 1180591620717411303u },
  {  8824922364862649494u, 1888946593147858085u }, {  7059937891890119595u, 1511157274518286468u },
  { 13026647942995916322u, 1208925819614629174u }, {  9774590264567735146u, 1934281311383406679u },
  { 11509021026396098440u, 1547425049106725343u }, { 16585914450600699399u, 1237940039285380274u },
  { 15469416676735388068u, 1980704062856608439u }, { 16064882156130220778u, 1584563250285286751u },
  {  9162556910162266299u, 1267650600228229401u }, {  7281393426775805432u, 2028240960365167042u },
  { 16893161185646375315u, 1622592768292133633u }, {  2446482504291369283u, 1298074214633706907u },
  {  7603720821608101175u, 2076918743413931051u }, {  2393627842544570617u, 1661534994731144841u },
  { 16672297533003297786u, 1329227995784915872u }, { 11918280793837635165u, 2126764793255865396u },
  {  5845275820328197809u, 1701411834604692317u }, { 15744267100488289217u, 1361129467683753853u },
  {  3054734472329800808u, 2177807148294006166u }, { 17201182836831481939u, 1742245718635204932u },
  {  6382248639981364905u, 1393796574908163946u }, {  2832900194486363201u, 2230074519853062314u },
  {  5955668970331000884u, 1784059615882449851u }, {  1075186361522890384u, 1427247692705959881u },
  { 12788344622662355584u, 2283596308329535809u }, { 13920024512871794791u, 1826877046663628647u },
  {  3757321980813615186u, 1461501637330902918u }, { 10384555214134712795u, 1169201309864722334u },
  {  5547241898389809503u, 1870722095783555735u }, {  4437793518711847602u, 1496577676626844588u },
  { 10928932444453298728u, 1197262141301475670u }, { 17486291911125277965u, 1915619426082361072u },
  {  6610335899416401726u, 1532495540865888858u }, { 12666966349016942027u, 1225996432692711086u },
  { 12888448528943286597u, 1961594292308337738u }, { 17689456452638449924u, 1569275433846670190u },
  { 14151565162110759939u, 1255420347077336152u }, {  7885109000409574610u, 2008672555323737844u },
  {  9997436015069570011u, 1606938044258990275u }, {  7997948812055656009u, 1285550435407192220u },
  { 12796718099289049614u, 2056880696651507552u }, {  2858676849947419045u, 1645504557321206042u },
  { 13354987924183666206u, 1316403645856964833u }, { 17678631863951955605u, 2106245833371143733u },
  {  3074859046935833515u, 1684996666696914987u }, { 13527933681774397782u, 1347997333357531989u },
  { 10576647446613305481u, 2156795733372051183u }, { 15840015586774465031u, 1725436586697640946u },
  {  8982663654677661702u, 1380349269358112757u }, { 18061610662226169046u, 2208558830972980411u },
  { 10759939715039024913u, 1766847064778384329u }, { 12297300586773130254u, 1413477651822707463u },
  { 15986332124095098083u, 2261564242916331941u }, {  9099716884534168143u, 1809251394333065553u },
  { 14658471137111155161u, 1447401115466452442u }, {  4348079280205103483u, 1157920892373161954u },
  { 14335624477811986218u, 1852673427797059126u }, {  7779150767507678651u, 1482138742237647301u },
  {  2533971799264232598u, 1185710993790117841u }, { 15122401323048503126u, 1897137590064188545u },
  { 12097921058438802501u, 1517710072051350836u }, {  5988988032009131678u, 1214168057641080669u },
  { 16961078480698431330u, 1942668892225729070u }, { 13568862784558745064u, 1554135113780583256u },
  {  7165741412905085728u, 1243308091024466605u }, { 11465186260648137165u, 1989292945639146568u },
  { 16550846638002330379u, 1591434356511317254u }, { 16930026125143774626u, 1273147485209053803u },
  {  4951948911778577463u, 2037035976334486086u }, {   272210314680951647u, 1629628781067588869u },
  {  3907117066486671641u, 1303703024854071095u }, {  6251387306378674625u, 2085924839766513752u },
  { 16069156289328670670u, 1668739871813211001u }, {  9165976216721026213u, 1334991897450568801u },
  {  7286864317269821294u, 2135987035920910082u }, { 16897537898041588005u, 1708789628736728065u },
  { 13518030318433270404u, 1367031702989382452u }, {  6871453250525591353u, 2187250724783011924u },
  {  9186511415162383406u, 1749800579826409539u }, { 11038557946871817048u, 1399840463861127631u },
  { 10282995085511086630u, 2239744742177804210u }, {  8226396068408869304u, 1791795793742243368u },
  { 13959814484210916090u, 1433436634993794694u }, { 11267656730511734774u, 2293498615990071511u },
  {  5324776569667477496u, 1834798892792057209u }, {  7949170070475892320u, 1467839114233645767u },
  { 17427382500606444826u, 1174271291386916613u }, {  5747719112518849781u, 1878834066219066582u },
  { 15666221734240810795u, 1503067252975253265u }, { 12532977387392648636u, 1202453802380202612u },
  {  5295368560860596524u, 1923926083808324180u }, {  4236294848688477220u, 1539140867046659344u },
  {  7078384693692692099u, 1231312693637327475u }, { 11325415509908307358u, 1970100309819723960u },
  {  9060332407926645887u, 1576080247855779168u }, { 14626963555825137356u, 1260864198284623334u },
  { 12335095245094488799u, 2017382717255397335u }, {  9868076196075591040u, 1613906173804317868u },
  { 15273158586344293478u, 1291124939043454294u }, { 13369007293925138595u, 2065799902469526871u },
  {  7005857020398200553u, 1652639921975621497u }, { 16672732060544291412u, 1322111937580497197u },
  { 11918976037903224966u, 2115379100128795516u }, {  5845832015580669650u, 1692303280103036413u },
  { 12055363241948356366u, 1353842624082429130u }, {   841837113407818570u, 2166148198531886609u },
  {  4362818505468165179u, 1732918558825509287u }, { 14558301248600263113u, 1386334847060407429u },
  { 12225235553534690011u, 2218135755296651887u }, {  2401490813343931363u, 1774508604237321510u },
  {  1921192650675145090u, 1419606883389857208u }, { 17831303500047873437u, 2271371013423771532u },
  {  6886345170554478103u, 1817096810739017226u }, {  1819727321701672159u, 1453677448591213781u },
  { 16213177116328979020u, 1162941958872971024u }, { 14873036941900635463u, 1860707134196753639u },
  { 15587778368262418694u, 1488565707357402911u }, {  8780873879868024632u, 1190852565885922329u },
  {  2981351763563108441u, 1905364105417475727u }, { 13453127855076217722u, 1524291284333980581u },
  {  7073153469319063855u, 1219433027467184465u }, { 11317045550910502167u, 1951092843947495144u },
  { 12742985255470312057u, 1560874275157996115u }, { 10194388204376249646u, 1248699420126396892u },
  {  1553625868034358140u, 1997919072202235028u }, {  8621598323911307159u, 1598335257761788022u },
  { 17965325103354776697u, 1278668206209430417u }, { 13987124906400001422u, 2045869129935088668u },
  {   121653480894270168u, 1636695303948070935u }, {    97322784715416134u, 1309356243158456748u },
  { 14913111714512307107u, 2094969989053530796u }, {  8241140556867935363u, 1675975991242824637u },
  { 17660958889720079260u, 1340780792994259709u }, { 17189487779326395846u, 2145249268790815535u },
  { 13751590223461116677u, 1716199415032652428u }, { 18379969808252713988u, 1372959532026121942u },
  { 14650556434236701088u, 2196735251241795108u }, {   652398703163629901u, 1757388200993436087u },
  { 11589965406756634890u, 1405910560794748869u }, {  7475898206584884855u, 2249456897271598191u },
  {  2291369750525997561u, 1799565517817278553u }, {  9211793429904618695u, 1439652414253822842u },
  { 18428218302589300235u, 2303443862806116547u }, {  7363877012587619542u, 1842755090244893238u },
  { 13269799239553916280u, 1474204072195914590u }, { 10615839391643133024u, 1179363257756731672u },
  {  2227947767661371545u, 1886981212410770676u }, { 16539753473096738529u, 1509584969928616540u },
  { 13231802778477390823u, 1207667975942893232u }, {  6413489186596184024u, 1932268761508629172u },
  { 16198837793502678189u, 1545815009206903337u }, {  5580372605318321905u, 1236652007365522670u },
  {  8928596168509315048u, 1978643211784836272u }, { 18210923379033183008u, 1582914569427869017u },
  {  7190041073742725760u, 1266331655542295214u }, {   436019273762630246u, 2026130648867672343u },
  {  7727513048493924843u, 1620904519094137874u }, {  9871359253537050198u, 1296723615275310299u },
  {  4726128361433549347u, 2074757784440496479u }, {  7470251503888749801u, 1659806227552397183u },
  { 13354898832594820487u, 1327844982041917746u }, { 13989140502667892133u, 2124551971267068394u },
  { 14880661216876224029u, 1699641577013654715u }, { 11904528973500979224u, 1359713261610923772u },
  {  4289851098633925465u, 2175541218577478036u }, { 18189276137874781665u, 1740432974861982428u },
  {  3483374466074094362u, 1392346379889585943u }, {  1884050330976640656u, 2227754207823337509u },
  {  5196589079523222848u, 1782203366258670007u }, { 15225317707844309248u, 1425762693006936005u },
  {  5913764258841343181u, 2281220308811097609u }, {  8420360221814984868u, 1824976247048878087u },
  { 17804334621677718864u, 1459980997639102469u }, { 17932816512084085415u, 1167984798111281975u },
  { 10245762345624985047u, 1868775676978051161u }, {  4507261061758077715u, 1495020541582440929u },
  {  7295157664148372495u, 1196016433265952743u }, {  7982903447895485668u, 1913626293225524389u },
  { 10075671573058298858u, 1530901034580419511u }, {  4371188443704728763u, 1224720827664335609u },
  { 14372599139411386667u, 1959553324262936974u }, { 15187428126271019657u, 1567642659410349579u },
  { 15839291315758726049u, 1254114127528279663u }, {  3206773216762499739u, 2006582604045247462u },
  { 13633465017635730761u, 1605266083236197969u }, { 14596120828850494932u, 1284212866588958375u },
  {  4907049252451240275u, 2054740586542333401u }, {   236290587219081897u, 1643792469233866721u },
  { 14946427728742906810u, 1315033975387093376u }, { 16535586736504830250u, 2104054360619349402u },
  {  5849771759720043554u, 1683243488495479522u }, { 15747863852001765813u, 1346594790796383617u },
  { 10439186904235184007u, 2154551665274213788u }, { 15730047152871967852u, 1723641332219371030u },
  { 12584037722297574282u, 1378913065775496824u }, {  9066413911450387881u, 2206260905240794919u },
  { 10942479943902220628u, 1765008724192635935u }, {  8753983955121776503u, 1412006979354108748u },
  { 10317025513452932081u, 2259211166966573997u }, {   874922781278525018u, 1807368933573259198u },
  {  8078635854506640661u, 1445895146858607358u }, { 13841606313089133175u, 1156716117486885886u },
  { 14767872471458792434u, 1850745787979017418u }, {   746251532941302978u, 1480596630383213935u },
  {   597001226353042382u, 1184477304306571148u }, { 15712597221132509104u, 1895163686890513836u },
  {  8880728962164096960u, 1516130949512411069u }, { 10793931984473187891u, 1212904759609928855u },
  { 17270291175157100626u, 1940647615375886168u }, {  2748186495899949531u, 1552518092300708935u },
  {  2198549196719959625u, 1242014473840567148u }, { 18275073973719576693u, 1987223158144907436u },
  { 10930710364233751031u, 1589778526515925949u }, { 12433917106128911148u, 1271822821212740759u },
  {  8826220925580526867u, 2034916513940385215u }, {  7060976740464421494u, 1627933211152308172u },
  { 16716827836597268165u, 1302346568921846537u }, { 11989529279587987770u, 2083754510274954460u },
  {  9591623423670390216u, 1667003608219963568u }, { 15051996368420132820u, 1333602886575970854u },
  { 13015147745246481542u, 2133764618521553367u }, {  3033420566713364587u, 1707011694817242694u },
  {  6116085268112601993u, 1365609355853794155u }, {  9785736428980163188u, 2184974969366070648u },
  { 15207286772667951197u, 1747979975492856518u }, {  1097782973908629988u, 1398383980394285215u },
  {  1756452758253807981u, 2237414368630856344u }, {  5094511021344956708u, 1789931494904685075u },
  {  4075608817075965366u, 1431945195923748060u }, {  6520974107321544586u, 2291112313477996896u },
  {  1527430471115325346u, 1832889850782397517u }, { 12289990821117991246u, 1466311880625918013u },
  { 17210690286378213644u, 1173049504500734410u }, {  9090360384495590213u, 1876879207201175057u },
  { 18340334751822203140u, 1501503365760940045u }, { 14672267801457762512u, 1201202692608752036u },
  { 16096930852848599373u, 1921924308174003258u }, {  1809498238053148529u, 1537539446539202607u },
  { 12515645034668249793u, 1230031557231362085u }, {  1578287981759648052u, 1968050491570179337u },
  { 12330676829633449412u, 1574440393256143469u }, { 13553890278448669853u, 1259552314604914775u },
  {  3239480371808320148u, 2015283703367863641u }, { 17348979556414297411u, 1612226962694290912u },
  {  6500486015647617283u, 1289781570155432730u }, { 10400777625036187652u, 2063650512248692368u },
  { 15699319729512770768u, 1650920409798953894u }, { 16248804598352126938u, 1320736327839163115u },
  {  7551343283653851484u, 2113178124542660985u }, {  6041074626923081187u, 1690542499634128788u },
  { 12211557331022285596u, 1352433999707303030u }, {  1091747655926105338u, 2163894399531684849u },
  {  4562746939482794594u, 1731115519625347879u }, {  7339546366328145998u, 1384892415700278303u },
  {  8053925371383123274u, 2215827865120445285u }, {  6443140297106498619u, 1772662292096356228u },
  { 12533209867169019542u, 1418129833677084982u }, {  5295740528502789974u, 2269007733883335972u },
  { 15304638867027962949u, 1815206187106668777u }, {  4865013464138549713u, 1452164949685335022u },
  { 14960057215536570740u, 1161731959748268017u }, {  9178696285890871890u, 1858771135597228828u },
  { 14721654658196518159u, 1487016908477783062u }, {  4398626097073393881u, 1189613526782226450u },
  {  7037801755317430209u, 1903381642851562320u }, {  5630241404253944167u, 1522705314281249856u },
  {   814844308661245011u, 1218164251424999885u }, {  1303750893857992017u, 1949062802279999816u },
  { 15800395974054034906u, 1559250241823999852u }, {  5261619149759407279u, 1247400193459199882u },
  { 12107939454356961969u, 1995840309534719811u }, {  5997002748743659252u, 1596672247627775849u },
  {  8486951013736837725u, 1277337798102220679u }, {  2511075177753209390u, 2043740476963553087u },
  { 13076906586428298482u, 1634992381570842469u }, { 14150874083884549109u, 1307993905256673975u },
  {  4194654460505726958u, 2092790248410678361u }, { 18113118827372222859u, 1674232198728542688u },
  {  3422448617672047318u, 1339385758982834151u }, { 16543964232501006678u, 2143017214372534641u },
  {  9545822571258895019u, 1714413771498027713u }, { 15015355686490936662u, 1371531017198422170u },
  {  5577825024675947042u, 2194449627517475473u }, { 11840957649224578280u, 1755559702013980378u },
  { 16851463748863483271u, 1404447761611184302u }, { 12204946739213931940u, 2247116418577894884u },
  { 13453306206113055875u, 1797693134862315907u }, {  3383947335406624054u, 1438154507889852726u }
};

static const uint64_t DOUBLE_POW5_SPLIT[326][2] = {
  {                    0u, 1152921504606846976u }, {                    0u, 1441151880758558720u },
  {                    0u, 1801439850948198400u }, {                    0u, 2251799813685248000u },
  {                    0u, 1407374883553280000u }, {                    0u, 1759218604441600000u },
  {                    0u, 2199023255552000000u }, {                    0u, 1374389534720000000u },
  {                    0u, 1717986918400000000u }, {                    0u, 2147483648000000000u },
  {                    0u, 1342177280000000000u }, {                    0u, 1677721600000000000u },
  {                    0u, 2097152000000000000u }, {                    0u, 1310720000000000000u },
  {                    0u, 1638400000000000000u }, {                    0u, 2048000000000000000u },
  {                    0u, 1280000000000000000u }, {                    0u, 1600000000000000000u },
  {                    0u, 2000000000000000000u }, {                    0u, 1250000000000000000u },
  {                    0u, 1562500000000000000u }, {                    0u, 1953125000000000000u },
  {                    0u, 1220703125000000000u }, {                    0u, 1525878906250000000u },
  {                    0u, 1907348632812500000u }, {                    0u, 1192092895507812500u },
  {                    0u, 1490116119384765625u }, {  4611686018427387904u, 1862645149230957031u },
  {  9799832789158199296u, 1164153218269348144u }, { 12249790986447749120u, 1455191522836685180u },
  { 15312238733059686400u, 1818989403545856475u }, { 14528612397897220096u, 2273736754432320594u },
  { 13692068767113150464u, 1421085471520200371u }, { 12503399940464050176u, 1776356839400250464u },
  { 15629249925580062720u, 2220446049250313080u }, {  9768281203487539200u, 1387778780781445675u },
  {  7598665485932036096u, 1734723475976807094u }, {   274959820560269312u, 2168404344971008868u },
  {  9395221924704944128u, 1355252715606880542u }, {  2520655369026404352u, 1694065894508600678u },
  { 12374191248137781248u, 2117582368135750847u }, { 14651398557727195136u, 1323488980084844279u },
  { 13702562178731606016u, 1654361225106055349u }, {  3293144668132343808u, 2067951531382569187u },
  { 18199116482078572544u, 1292469707114105741u }, {  8913837547316051968u, 1615587133892632177u },
  { 15753982952572452864u, 2019483917365790221u }, { 12152082354571476992u, 1262177448353618888u },
  { 15190102943214346240u, 1577721810442023610u }, {  9764256642163156992u, 1972152263052529513u },
  { 17631875447420442880u, 1232595164407830945u }, {  8204786253993389888u, 1540743955509788682u },
  {  1032610780636961552u, 1925929944387235853u }, {  2951224747111794922u, 1203706215242022408u },
  {  3689030933889743652u, 1504632769052528010u }, { 13834660704216955373u, 1880790961315660012u },
  { 17870034976990372916u, 1175494350822287507u }, { 17725857702810578241u, 1469367938527859384u },
  {  3710578054803671186u, 1836709923159824231u }, {    26536550077201078u, 2295887403949780289u },
  { 11545800389866720434u, 1434929627468612680u }, { 14432250487333400542u, 1793662034335765850u },
  {  8816941072311974870u, 2242077542919707313u }, { 17039803216263454053u, 1401298464324817070u },
  { 12076381983474541759u, 1751623080406021338u }, {  5872105442488401391u, 2189528850507526673u },
  { 15199280947623720629u, 1368455531567204170u }, {  9775729147674874978u, 1710569414459005213u },
  { 16831347453020981627u, 2138211768073756516u }, {  1296220121283337709u, 1336382355046097823u },
  { 15455333206886335848u, 1670477943807622278u }, { 10095794471753144002u, 2088097429759527848u },
  {  6309871544845715001u, 1305060893599704905u }, { 12499025449484531656u, 1631326116999631131u },
  { 11012095793428276666u, 2039157646249538914u }, { 11494245889320060820u, 1274473528905961821u },
  {   532749306367912313u, 1593091911132452277u }, {  5277622651387278295u, 1991364888915565346u },
  {  7910200175544436838u, 1244603055572228341u }, { 14499436237857933952u, 1555753819465285426u },
  {  8900923260467641632u, 1944692274331606783u }, { 12480606065433357876u, 1215432671457254239u },
  { 10989071563364309441u, 1519290839321567799u }, {  9124653435777998898u, 1899113549151959749u },
  {  8008751406574943263u, 1186945968219974843u }, {  5399253239791291175u, 1483682460274968554u },
  { 15972438586593889776u, 1854603075343710692u }, {   759402079766405302u, 1159126922089819183u },
  { 14784310654990170340u, 1448908652612273978u }, {  9257016281882937117u, 1811135815765342473u },
  { 16182956370781059300u, 2263919769706678091u }, {  7808504722524468110u, 1414949856066673807u },
  {  5148944884728197234u, 1768687320083342259u }, {  1824495087482858639u, 2210859150104177824u },
  {  1140309429676786649u, 1381786968815111140u }, {  1425386787095983311u, 1727233711018888925u },
  {  6393419502297367043u, 2159042138773611156u }, { 13219259225790630210u, 1349401336733506972u },
  { 16524074032238287762u, 1686751670916883715u }, { 16043406521870471799u, 2108439588646104644u },
  {   803757039314269066u, 1317774742903815403u }, { 14839754354425000045u, 1647218428629769253u },
  {  4714634887749086344u, 2059023035787211567u }, {  9864175832484260821u, 1286889397367007229u },
  { 16941905809032713930u, 1608611746708759036u }, {  2730638187581340797u, 2010764683385948796u },
  { 10930020904093113806u, 1256727927116217997u }, { 18274212148543780162u, 1570909908895272496u },
  {  4396021111970173586u, 1963637386119090621u }, {  5053356204195052443u, 1227273366324431638u },
  { 15540067292098591362u, 1534091707905539547u }, { 14813398096695851299u, 1917614634881924434u },
  { 13870059828862294966u, 1198509146801202771u }, { 12725888767650480803u, 1498136433501503464u },
  { 15907360959563101004u, 1872670541876879330u }, { 14553786618154326031u, 1170419088673049581u },
  {  4357175217410743827u, 1463023860841311977u }, { 10058155040190817688u, 1828779826051639971u },
  {  7961007781811134206u, 2285974782564549964u }, { 14199001900486734687u, 1428734239102843727u },
  { 13137066357181030455u, 1785917798878554659u }, { 11809646928048900164u, 2232397248598193324u },
  { 16604401366885338411u, 1395248280373870827u }, { 16143815690179285109u, 1744060350467338534u },
  { 10956397575869330579u, 2180075438084173168u }, {  6847748484918331612u, 1362547148802608230u },
  { 17783057643002690323u, 1703183936003260287u }, { 17617136035325974999u, 2128979920004075359u },
  { 17928239049719816230u, 1330612450002547099u }, { 17798612793722382384u, 1663265562503183874u },
  { 13024893955298202172u, 2079081953128979843u }, {  5834715712847682405u, 1299426220705612402u },
  { 16516766677914378815u, 1624282775882015502u }, { 11422586310538197711u, 2030353469852519378u },
  { 11750802462513761473u, 1268970918657824611u }, { 10076817059714813937u, 1586213648322280764u },
  { 12596021324643517422u, 1982767060402850955u }, {  5566670318688504437u, 1239229412751781847u },
  {  2346651879933242642u, 1549036765939727309u }, {  7545000868343941206u, 1936295957424659136u },
  {  4715625542714963254u, 1210184973390411960u }, {  5894531928393704067u, 1512731216738014950u },
  { 16591536947346905892u, 1890914020922518687u }, { 17287239619732898039u, 1181821263076574179u },
  { 16997363506238734644u, 1477276578845717724u }, {  2799960309088866689u, 1846595723557147156u },
  { 10973347230035317489u, 1154122327223216972u }, { 13716684037544146861u, 1442652909029021215u },
  { 12534169028502795672u, 1803316136286276519u }, { 11056025267201106687u, 2254145170357845649u },
  { 18439230838069161439u, 1408840731473653530u }, { 13825666510731675991u, 1761050914342066913u },
  {  3447025083132431277u, 2201313642927583642u }, {  6766076695385157452u, 1375821026829739776u },
  {  8457595869231446815u, 1719776283537174720u }, { 10571994836539308519u, 2149720354421468400u },
  {  6607496772837067824u, 1343575221513417750u }, { 17482743002901110588u, 1679469026891772187u },
  { 17241742735199000331u, 2099336283614715234u }, { 15387775227926763111u, 1312085177259197021u },
  {  5399660979626290177u, 1640106471573996277u }, { 11361262242960250625u, 2050133089467495346u },
  { 11712474920277544544u, 1281333180917184591u }, { 10028907631919542777u, 1601666476146480739u },
  {  7924448521472040567u, 2002083095183100924u }, { 14176152362774801162u, 1251301934489438077u },
  {  3885132398186337741u, 1564127418111797597u }, {  9468101516160310080u, 1955159272639746996u },
  { 15140935484454969608u, 1221974545399841872u }, {   479425281859160394u, 1527468181749802341u },
  {  5210967620751338397u, 1909335227187252926u }, { 17091912818251750210u, 1193334516992033078u },
  { 12141518985959911954u, 1491668146240041348u }, { 15176898732449889943u, 1864585182800051685u },
  { 11791404716994875166u, 1165365739250032303u }, { 10127569877816206054u, 1456707174062540379u },
  {  8047776328842869663u, 1820883967578175474u }, {   836348374198811271u, 2276104959472719343u },
  {  7440246761515338900u, 1422565599670449589u }, { 13911994470321561530u, 1778206999588061986u },
  {  8166621051047176104u, 2222758749485077483u }, {  2798295147690791113u, 1389224218428173427u },
  { 17332926989895652603u, 1736530273035216783u }, { 17054472718942177850u, 2170662841294020979u },
  {  8353202440125167204u, 1356664275808763112u }, { 10441503050156459005u, 1695830344760953890u },
  {  3828506775840797949u, 2119787930951192363u }, {    86973725686804766u, 1324867456844495227u },
  { 13943775212390669669u, 1656084321055619033u }, {  3594660960206173375u, 2070105401319523792u },
  {  2246663100128858359u, 1293815875824702370u }, { 12031700912015848757u, 1617269844780877962u },
  {  5816254103165035138u, 2021587305976097453u }, {  5941001823691840913u, 1263492066235060908u },
  {  7426252279614801142u, 1579365082793826135u }, {  4671129331091113523u, 1974206353492282669u },
  {  5225298841145639904u, 1233878970932676668u }, {  6531623551432049880u, 1542348713665845835u },
  {  3552843420862674446u, 1927935892082307294u }, { 16055585193321335241u, 1204959932551442058u },
  { 10846109454796893243u, 1506199915689302573u }, { 18169322836923504458u, 1882749894611628216u },
  { 11355826773077190286u, 1176718684132267635u }, {  9583097447919099954u, 1470898355165334544u },
  { 11978871809898874942u, 1838622943956668180u }, { 14973589762373593678u, 2298278679945835225u },
  {  2440964573842414192u, 1436424174966147016u }, {  3051205717303017741u, 1795530218707683770u },
  { 13037379183483547984u, 2244412773384604712u }, {  8148361989677217490u, 1402757983365377945u },
  { 14797138505523909766u, 1753447479206722431u }, { 13884737113477499304u, 2191809349008403039u },
  { 15595489723564518921u, 1369880843130251899u }, { 14882676136028260747u, 1712351053912814874u },
  {  9379973133180550126u, 2140438817391018593u }, { 17391698254306313589u, 1337774260869386620u },
  {  3292878744173340370u, 1672217826086733276u }, {  4116098430216675462u, 2090272282608416595u },
  {   266718509671728212u, 1306420176630260372u }, {   333398137089660265u, 1633025220787825465u },
  {  5028433689789463235u, 2041281525984781831u }, { 10060300083759496378u, 1275800953740488644u },
  { 12575375104699370472u, 1594751192175610805u }, {  1884160825592049379u, 1993438990219513507u },
  { 17318501580490888525u, 1245899368887195941u }, {  7813068920331446945u, 1557374211108994927u },
  {  5154650131986920777u, 1946717763886243659u }, {   915813323278131534u, 1216698602428902287u },
  { 14979824709379828129u, 1520873253036127858u }, {  9501408849870009354u, 1901091566295159823u },
  { 12855909558809837702u, 1188182228934474889u }, {  2234828893230133415u, 1485227786168093612u },
  {  2793536116537666769u, 1856534732710117015u }, {  8663489100477123587u, 1160334207943823134u },
  {  1605989338741628675u, 1450417759929778918u }, { 11230858710281811652u, 1813022199912223647u },
  {  9426887369424876662u, 2266277749890279559u }, { 12809333633531629769u, 1416423593681424724u },
  { 16011667041914537212u, 1770529492101780905u }, {  6179525747111007803u, 2213161865127226132u },
  { 13085575628799155685u, 1383226165704516332u }, { 16356969535998944606u, 1729032707130645415u },
  { 15834525901571292854u, 2161290883913306769u }, {  2979049660840976177u, 1350806802445816731u },
  { 17558870131333383934u, 1688508503057270913u }, {  8113529608884566205u, 2110635628821588642u },
  {  9682642023980241782u, 1319147268013492901u }, { 16714988548402690132u, 1648934085016866126u },
  { 11670363648648586857u, 2061167606271082658u }, { 11905663298832754689u, 1288229753919426661u },
  {  1047021068258779650u, 1610287192399283327u }, { 15143834390605638274u, 2012858990499104158u },
  {  4853210475701136017u, 1258036869061940099u }, {  1454827076199032118u, 1572546086327425124u },
  {  1818533845248790147u, 1965682607909281405u }, {  3442426662494187794u, 1228551629943300878u },
  { 13526405364972510550u, 1535689537429126097u }, {  3072948650933474476u, 1919611921786407622u },
  { 15755650962115585259u, 1199757451116504763u }, { 15082877684217093670u, 1499696813895630954u },
  {  9630225068416591280u, 1874621017369538693u }, {  8324733676974063502u, 1171638135855961683u },
  {  5794231077790191473u, 1464547669819952104u }, {  7242788847237739342u, 1830684587274940130u },
  { 18276858095901949986u, 2288355734093675162u }, { 16034722328366106645u, 1430222333808546976u },
  {  1596658836748081690u, 1787777917260683721u }, {  6607509564362490017u, 2234722396575854651u },
  {  1823850468512862308u, 1396701497859909157u }, {  6891499104068465790u, 1745876872324886446u },
  { 17837745916940358045u, 2182346090406108057u }, {  4231062170446641922u, 1363966306503817536u },
  {  5288827713058302403u, 1704957883129771920u }, {  6611034641322878003u, 2131197353912214900u },
  { 13355268687681574560u, 1331998346195134312u }, { 16694085859601968200u, 1664997932743917890u },
  { 11644235287647684442u, 2081247415929897363u }, {  4971804045566108824u, 1300779634956185852u },
  {  6214755056957636030u, 1625974543695232315u }, {  3156757802769657134u, 2032468179619040394u },
  {  6584659645158423613u, 1270292612261900246u }, { 17454196593302805324u, 1587865765327375307u },
  { 17206059723201118751u, 1984832206659219134u }, {  6142101308573311315u, 1240520129162011959u },
  {  3065940617289251240u, 1550650161452514949u }, {  8444111790038951954u, 1938312701815643686u },
  {   665883850346957067u, 1211445438634777304u }, {   832354812933696334u, 1514306798293471630u },
  { 10263815553021896226u, 1892883497866839537u }, { 17944099766707154901u, 1183052186166774710u },
  { 13206752671529167818u, 1478815232708468388u }, { 16508440839411459773u, 1848519040885585485u },
  { 12623618533845856310u, 1155324400553490928u }, { 15779523167307320387u, 1444155500691863660u },
  {  1277659885424598868u, 1805194375864829576u }, {  1597074856780748586u, 2256492969831036970u },
  {  5609857803915355770u, 1410308106144398106u }, { 16235694291748970521u, 1762885132680497632u },
  {  1847873790976661535u, 2203606415850622041u }, { 12684136165428883219u, 1377254009906638775u },
  { 11243484188358716120u, 1721567512383298469u }, {   219297180166231438u, 2151959390479123087u },
  {  7054589765244976505u, 1344974619049451929u }, { 13429923224983608535u, 1681218273811814911u },
  { 12175718012802122765u, 2101522842264768639u }, { 14527352785642408584u, 1313451776415480399u },
  { 13547504963625622826u, 1641814720519350499u }, { 12322695186104640628u, 2052268400649188124u },
  { 16925056528170176201u, 1282667750405742577u }, {  7321262604930556539u, 1603334688007178222u },
  { 18374950293017971482u, 2004168360008972777u }, {  4566814905495150320u, 1252605225005607986u },
  { 14931890668723713708u, 1565756531257009982u }, {  9441491299049866327u, 1957195664071262478u },
  {  1289246043478778550u, 1223247290044539049u }, {  6223243572775861092u, 1529059112555673811u },
  {  3167368447542438461u, 1911323890694592264u }, {  1979605279714024038u, 1194577431684120165u },
  {  7086192618069917952u, 1493221789605150206u }, { 18081112809442173248u, 1866527237006437757u },
  { 13606538515115052232u, 1166579523129023598u }, {  7784801107039039482u, 1458224403911279498u },
  {   507629346944023544u, 1822780504889099373u }, {  5246222702107417334u, 2278475631111374216u },
  {  3278889188817135834u, 1424047269444608885u }, {  8710297504448807696u, 1780059086805761106u }
};

#endif // RYU_D2S_FULL_TABLE_H
