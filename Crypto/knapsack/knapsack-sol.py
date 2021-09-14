from Crypto.Util.number import inverse, GCD
from itertools import product

#vars

b = [15611, 1894756, 355366474, 34126743663, 5944658626288, 475502210401836, 92737445336690517, 13753198649308199810, 3118187255966192737810, 419848772609076220078250, 2667917901147380506878472, 63335683657323974636433321, 9112909243190356511357664040, 813145274630122335762503812192, 136716561058889218692010314315581, 15432445943100588778101367894911062, 3237510366152610632465432578110422935, 582149731986051897973175672138065109674, 76092022284197569733259499848631206520150, 6215008735797707079082529645598786997900463, 1318178090329737276206181946597031720665903152, 36998726139439004044327751077245649359252297476, 4743978350710850384936349949735463554084740052413, 1049050979680591985899783670580023826773816378640651, 203348449374994840342381551649778504322965747768741667, 19898639989731157909445295580192144632935077592946920216, 3832130898063131457671655904892707813125282548433530352098, 457015448783048726239407007768991666406560346699788209206913, 47730922943255771145579696587190920005213998327594604711992291, 658945470340948079094016859143881252338950922289579286256226884, 95035466911513423053819980459489783450884064407625248879968250302, 8109112212294710303558370955351221363287796150175708736666317859362, 907537230852079081775216716178627319371304516694513627433139693528831, 119765457140444894921545194526888335884941229857841201779188820397898260, 16583715325656488194939767887877160649635109739500965426979088242967430977, 2683138864779633134292231430400004602346974795959640129105917177989469156925, 74404969818242013249333767165803499471215780991470642552827972674047592641306, 9475888320387991372850237498293733993959539108881357181819402821481594817460997, 871708052713301478422986477471926996797401123161261424868103049930925571240760802, 102133429571197928190897665183893101536927396914951557832714328019241671800918850120, 6941116149455598916189311719466728806060318191496619086822466248990698674430100570477, 792912047391117560384800758982544466251678700318792283806254230302697761157499696710055, 104621026022714977382417910254886018104229897855306049785826263584331186302621523907848088, 23778859741067782662960447566839659175584468931380700992592140511329338496822845378073881318, 2456479792277181556289679120312192334404742651608389775389760683154517803129106145510607063117, 388705045971527015397317868595374518266833390662398521294461905699556335413378490455180955452720, 63793035767849248536437284007130388234385307356093039776561097747853147046927309346690904180881910, 6581679406335668087105348691830533737787012125631171599525455932522804792048681345843357119055939866, 1531205034726940849490192646530023477622615812630980898282859399591892290688274527618387852929906583127, 183707785766715804535196616706375006332108328042209633571010495102568714271666704860394644623570998664062, 32876504552240921412377498729482458785602759802810305808673275637755332487956011614963080861874647144406251, 7415999081328992985429733492448983090069772139888077483725030154803639830362550221822259447010061762985123490, 1294402085009197570685679355812976716754589052123847837573643484498648227151326552619729055771603495127219376769, 193121771374728904868507915373844494987257296775779171302712581946977399896644905532110997526041219177232937383518, 2475142483638529864823255180268925203607722684711945909416524206128014723059676813420037981730627630974299694141043, 475686770140256937210086864436823755176925760572143007678206559951908526312774987234904153151788845602674036029811100, 77585568689608365498336269835162077425373384759864175398807979511441923554316423907782941825552057428840857589052433284, 13247355914133019784438753735408719185329086380918539888343279476784878911817742909497209700301428525555612268308263232588, 254812685915119382251175551059524021182182502374080198935575810053724321331891437376143760142538844887834266714960633029430, 52890865707965438750875250819007367242586356947460893564278407278088667782647245544111566341746886270268159496991727215544429, 11217727180242090988876969026365733040130428219712997952950912928048192367891041435339262634225488728175786920418714358083088452, 1033651195331991682193744543283191298521690205057608684507995892533993977889269034670563475719845860030510120093466753042397664942, 21331572332354095063945517316229482296016211289946841413864876428898011567444967335672209991727157674664402337537506871677033743558, 328913190558699520087271555891086032626997136341325749471346858977061291060910926397457446781528440017655353610800437255537579096435, 41016405078354757530155936871098937034193860684850990672642743000869115212614630618810149686444222985317400917514858056190319536162008, 9468202583151409390159478449787787236724499083028213552676298859158520919782792558746542765976692409188371555886691214741652087985390448, 1209370733325414597380402195614072308300647530898688590873073903362295053528340613355058326522692558569485360265860293328202563566914376654, 244896284066159293777567711722891777134209641910312161034289653239647995045925735187127327266738402391091305043085978804760346584239975646825, 14041283732812775801822976976809949839613861856371452909212564087563993930118549604449183446550197950195758797106878273023174166466460300364754, 3157724958013383651696079652583662792904187518204201834935596458442100173518625727079734174277716621752316131430053223205390542349237580421480772, 243044306132337288780809489219645171374366907965658767985305823521544249194399530169961779270831096542548798742930540880769729202066169375317862962, 2053579075553430846142840363071892634024402096896375680856062255739195349998963838258240283676921230528692540115523700373471242132258862216809476196, 14455798500500918284128934181343421664555728859634221882206823150266711089911984647440451735532025507840054158918834633226763664763956191655320656642, 2463832483533220172330432078859083328050348205344532927190015046192830123070267845804822552157564913408523383062186067158617149128132627209578510000215, 142249750394333665179148368561293056170712744903332144204175345926380253124815980077778863572568308945796182881238678804572547330022561298195936331260050, 17501392613590114731838711460831859738174556283707234535876798244154564143424537311778003420760470038270558172511693636563049003983924741356580222494815395, 4009604290622461957925629270434934326829437143099179383741142935422092949685969102852568177412912848043319594923474320525581789199937031773983493755984461791, 294193712116622709478475483301365819854103301081409209452731459473321925992203302461080877662842144276561397270322383970006828802741034004259703423136091061545, 51392905607546125477908752327040522994271280189391601935706909194192585671409074042366269431189219358434722530884751196105294724598899320734370030921877516123939, 6859213413374970093990814093601451131622059902017962699366823865462102814245162553257592680647687179090173865841984358027079961611314326412463866100205138119221645, 917026754743196150702663895907835899418770712607579189749851252768964300613621989870631671061204105787289422176086951786867877085261539428985513701768808071007084207, 14358009235321525311950572220320901322285179382724633066127304027677389603370943501465994716511030577676576720723325965121015208368058940690945941054559020293541033075, 2390666194208007812791290357125699843069321529775418782202954316910560424503561589622759449277099524062165817467914044322695693464287720206229967352791809808366673203984, 382878291434907068347295724907376346632710546258877769782528080622950335561589296277673327021484227351270078723977599918563205175431719168578301632068841228222435229870471, 83630226093361174279477424320755183140893158838323770884455599751929096573252675826733774008391798872225388988325460529418645063357626490625783521273225953092499653640092790, 2932472278238717646178826535766437078795043772835811393749648033982516100503115246796817218734096676714041318719725062021488736035519216856998326910191879748758511566348261465, 140802636399247782075112115116290058710846374528097731608176410872960277173761586778945649444816214690680956949694861737739927387325315611880782295944241606879320462148151686217, 2650265992768278499152604036959680638613975274568210233716130191155236775464062064225610766478780685326639902004060794001242429396510601847213272106929901329013565946982891522739, 295633596764918879808520262512964145717611611985381979450858524651838863774580263951960630940421329299125408500933813604001777360865623540537853729941379213744738350542978955186991, 63093653360169775360617990071420798341558065258734174961111923039195093620281123065026026451555876688935758329683525070851657233686217477567466237455001051043079911480200730507556194, 1093213412338515907428353244195189592316223476318507011070906101331406898017493271124385290850967701966795965934146813580639930339394996474084423820532050336012455332317554244851117891, 206414564609546264258163183013254891752001283825227405044054227263278912115650368263484067263691258096342741402361845087462120896418509604009243318010008097611901232025397328643833814653, 7801728970688617395060684049665303005630947022956178421425874050802609987832225450085621333485389931074562103279934745148451279126721298809140156670258261228252414670085699807802285657998, 1464611684899106765741252169929128129119096369152552801579992687078208692390636045502025260114188782323560648093596353722586858850699021958072818206149527970012345589530640191808164152612034, 55289897268647516936736605361680368083726159231054782770053521853730987631436295831403514742290106661373339065878475646411112367341033506358165304926377404218541542693958384877228771289506351, 3932340530607630783402149570277003071841639422262503502231582962509009415452715444191026354681171245085262713079572434032817601296714935952238206155147361149500991486358459425910504973673909930, 395266246410254035282697368580357594986513383760639190193294741230324959406447069422812423681410297329565010576461205410446113273179396402488801940208898444359870790587062809265337890067516866385, 16904694589421429728955731371942665531256873566191052152078828864972144321699156890593313105832334320415753402432822131899933635191316981972405726106052590278585709748094776871158207063800274192266, 2342571730529415338583646072102462122466312839274845477600457647880114762542027620780524713780299979070056734295099437613847626233095586499090819737403023250202538526022584597448469752907899247325477, 501368028746777493093666201568539051140303819916039401729501473476418848888191871115933080883255752807498705829212827120308399901036796629588822119300378259340252602412975733919627329712257489097342334, 52700250916373936428362422887912520721923903469098296261040920158604312942809834295608717768624612451844258512216652682738266878353520514802932134856691824150418561175936863894119007417307310105966336706, 10936834644069985025638951207349975858772373222882126699078440513719807313489212582280423107246877513340305232779500594746970974440215383593573055698241440891429788160844380390545779197283866858724900810355, 2266119626133267560330728728222707198010439840619193036515555314270388929223950931895350887682590430504484217079690764537082319710956041154297713488386324496131678782665164283338378679081244181469111154740302, 345373015866386137831340259056333333130831896229726177194385318870839089495704502096071355763100606994726257159307635034488149963235802669499870307801354854250745426928430145101726663613434604433803620211546249, 20404570536772110832523801180279823246633288913803682898061399354775643635788547767192586763283972384735676981257990489498584274276602008477139233760067587298601231193254802712182552078672819681615654142503634549, 527402938356209079310860859696833878898993989627424944821845489969577378920695353062231248833797577548010141286262985496126859396877881577143869976915146360214069831619398805780682417025160276096651522339324459406, 86872470161751976080977438690902120962029544467167341528713019183312950037747501947859290884073689689400225184600352595717451713509467425600401846110225769127320830210316282460390454444990314299995201497330275203014, 17734548725548887380184729779949026000361120156246937564998112149389004690415022004500164576459830910785494803030724997462671046808796784378531278020552135471501862659722863635198267683164941226264169207592641952998868, 3096974654102256613350834289995071286218008197812812815654222012345281693254974422009221837709261695080075577794906492204417348910327422852631099273009278650976927546565467615341916715413897765450157533877559286129132592, 64610723671907209392232740477304296413954539648936071417447195341718899811449243682105712592200015656271260346837445093715465883003358379989612548456357422009884468565016801936355551732844931251191006769976125169093547079, 12458299291226265154795286745931242943470458899517272679384360512595404591375097616776278786773347181526146400456848441430035485799455006180193025326316267820372640958162708296000406192858473057313724591511630204169509038817, 636824913650057489232206121893643578575000345856412966239866791296157681154721911640746786704073032585312960044729548636200442473938480755162874978706804667112989446004017824675816860055073561804626748338654174981173717146358, 121364982519308636748266203789858610610126737565373432065917190758444402303512245453227962916651580160972594078580328216604709480698503887519365102791347922613403680052198036978671660750043751413713164945582387828079526910538365, 5312860035881029152563480424344190335788356084591507109874557137269657478836407621294908587561438554372320476864878659917001728728251751891093508657688302013741733331370724027747981609120672568142511677147377917628904430898512728, 22886762860109047267160204279144138789173651287370913114499850610505331805419130206490364268480720754092708249980056839865219777815411064801274795215503240931632527264312896307504353743265458501786841142503306352342323052121278012, 4312641555823431347378292449669639821277074426434608255604845200485717721577746915796918133934587373718489487924050787921882461966500611057072195121215265108597136515650177197137607391103628732859796719924900816186646932194910470513, 478676871173335810753661792145027456513352026279373174136574854716644730609334368002828458248864282072523449834375891325981368362489085966072962077293977244291354765456022602963713878717543265505793689162449286379333118630695605272645, 19384327400583828111753424504564698570502602418456360792847135788790978227938008465500986772322584498719921450402621563901342955849831440950298578654415087721991556499811668398926242393139305845990406356594263016202255501489725538153153, 3513871347907794842511464639973788593424901799774519304763713777731254150893937011263387575924038043398017168255550932500142495023145996341195635466222231568988121805788274418509849254147783891693306043041146999018525881111436477404540108, 752283208554364020396816358254678242336945073726860537493917640974551473012458025216212495352058423281967546895419058002277137600399048090079970715456235279049524563708891349147769633922345847696374868349355899141394323620362833349119843648, 141026018210139572265540586894699181226719757323968641351756813359519021671089403594535499910946743457859478135391174113758493617247419101164294763411499216730404728332980817805422232020214956433992709873533731759199491871364531102935578297947, 3093311668459944124745153557105415903816031139577246088705358062004931272406003841122961789650133065554174345490591738081340833550388053864632757251331352266970499037358447597336056072479709274833253104002407587809324833499657973330867822823104, 560660674603170812585593549607976698637402555761018667629194085381595320244031178034399044200259834486796460641243159847190169573103747012336042068444542520219990812110872670026832634390668404427625640496925644485138936076102708124641847850649723, 18814350042254997208554844691250704784983484102582919913849698990653368809890984588517345825226160971949554554855774946545262226533628115372219151799802563638763068466073763236466548609260488777505958278201844875168189916153820738982429423950407814, 4330624837505639249882586595669312179631367477922155525270230056518311474461150831839882592617350098226480908503669253435008131080924466526546688319062092803983817265893527744191723487459675934619465367445221787560426418923058332689385350274454567249, 394584278098824431848123676878426887696800703427856429013563061086353596865118317383900764248752080188813776441788666981794640324230204706788911630320384161827625461508053637045890778827317668956952519326242767311620056662207257994463735197461336652616, 64178559477533253792450499278769556457417577813165585620203563527755677053408825353725046759477686366078650200243179572564724882512988484038283949402410133711181326802663193767464981174370882383896223288626746135012735808074668274717789609261036368713833, 8219885697348156532275939814959664000034544742649897194658243591483933599910898240057098122142255258733410467483088469776368418646486641841523676656900828462518692807110943571844271028617429391349909893269854355645943263547915942446054486538143987922822065, 1079790535980893647951298038496419428472275354803013260969767940213941009612423756389720591616846952244456185113415881745084367079122769059979883209974315231901749316932327720156414584567134764103804158344811883757607794479692366482010033032771078480446650856, 167968080836309484886700000084502655207671786555643769434154572925705039472142440133432171865841146638447159780351984406888613224223608894033804572974526430277245502944965359175757447542530284247595817121441940196180298319416699276945418399017406412232725627644, 17668359648755211988362304724808975985619196322790812946404109213401310738761710537560096565002834852349106088760073817227835323686478509111614549754993913342845508348441374042545190702528612995431102967878352093075824697573556516904615269555856082931484188117862, 2696608307901121727085889648687430249094404640958992889860147909205418125617976120007877472095061456672775387203154430214827445583807038474322945148036380641502913779941854691212080343768389462106367542639135481199557462662993849655957122550984669459745658265766368, 365867127550365607735791619163187637580989614815226704263354443957211141866170643307310769611052235210313386654407837120821938174564462730556035647685056633155825799970883270634918198392170565412583380076616121545234033117132432269007780738781879250552089494262052039, 23751407974627769549356958831812217230292475141119871743068323698619078800501894311946518308530794190339195546144314688088117614064399592006257100894091041764771076652782731810544456886263496043153039543826983296184907272380359629880452790157207095520208445834485907276, 3216403027604785890401271369829457917506940709939710551937638949831185263747248970289381572894064582730132870293570435870026333192058998639202370674857291295267956407559417664085885246201636052108201322032824686084255447733788730583131558607664050782791350488607545046435, 656250415213710033992075570947114609656725395060609534657922151393789201440960529520913381913420704328296535157476321335984035238252512282779961736857042470845576728732600057976182309879540864502587149273575635173165200360048498757185443360941779344334067757450643462615813, 50051958113242048567272133690447719228999715327462185616406709022347040964503394218182211260747081209504075468296033302878296519736279309066492090219343051762947375062639841812346367418143131551500069788296717149570614084787227114196219968350301528716099566716334051927938181, 10035374315151851131918987297338637853849205876100932745114999505349317061010811414092456615253728648831405849073779723258946379389801794173289589022474186271364629887171904474392474532218455337678057579763337269260879487685222313217622702837031391339180813210126542378130676325, 1360863632790357666444660835900834813269085184884640884412830821779630149160260655066799102624348753272760217285658632714893770143144779308968474045714037427419489107404972648440015054650300401784643481656706980436659639137935922969869735280034747686145500644584205637664110578008, 240255203465385139813697556280754448203022197722970406761553391355201065864092500705000347327438360267233230717928139610283709111244497984444333750621940104390034447737373107812486893666088528141257044654431237472845854099224820653139196067743828971173352456206845889342870750257, 1045140083807572168825905366655965154635144101589878086822439406769795276184182839984867096778772129721775248201692850897103208630823517651674033409762657002851843351777996633203560109758592037621022336739025552073198570603144085012247635149526558571654927064752964494734193745145, 492620953986941243822404576710605154734385506365033833570498057500028781182427383585499797647321054988240108681556198981746008991072693739196879706453923601766670100939840952437612037665155342103397832357093315653124495718323252012123322536212511661783211252907205831425493209654, 60748404785489145696714549960789159759327504545438387378854061972977100728173078892359736128102552435399154525573636170887129236989239031311318458732452184233618121877650677649739739741743307304954175427872527172873425476498357337577935948421418528816510910885411269434265320140, 423374205101876047588895798470639656258928777399372415446959858698518257227454072128114960306392589368369623954457541269226922175938214388289301730989780122052644495416585592401920115224228174823669115240014184055372723442714279650261482110666714827738971480538017092644792995946, 792953067645542052142483736006339800150730926086425871712057049904470543475839829095749258647195200493442119108975308574833838606608906841698713087111510398721957948458426982692570508708811432051144882406763464524304394709711043473712503766722771612447931441987549040196725736049, 1189500086446188891816999363148382589922463573699549951005449206892718060448272972994096882615575358649571113539689262306244112512282636393035702714396122919949528808873231097388122842912245368800933971396820586816957555264460274920664841764283249714321360804845656705272658552397, 1357817671091091818070771934720252957003517239120262882854667347770977971889396999135681550770243516065508139200051369256352703476910981597189088592717549714721834987177980000728234804615632580187855957419576573503442461944752322939629484946757526934556390596929439200400386710652, 648450466907864141434402200349099286276822859685594816684940101477239165482692734320043547700125688048947791119758602788488828378590395140295628343635295379601083514860432848728123979494484089244280944391325320828956145971856987668981812974137164948743461508316421668975231516374, 333422051766573309846283400541037109066146681043946582793177550401738226652030071649366357822172276646869779573608778949167819366227895470754806741786585643366468511448447871387138277640667292606752359821644231587128525234179171930903297912622760238267334404342564758229182626637, 929854776524205035298466710968355767610440445636728236700395543958459114129218422220908944013179214270926964954546463767699637120171278498115228014197916789681554843097592361953408405456266395217039983567621338097144517446718476674888220576590920364619385136081289044266167850228, 867813284461609144337408188214713797758542637658716001449809964766816410121439085018069836843664577204820887933821697640119772821049296688672591570858427646124183487416904667688582602414250365003151022427822296240606740704749198378257032734673209334512177388712150051260345008593, 89425860888095006338068125495990368305545945386802458719575203336643599653910024394824001717726679992823576543194954333241613418882505638468438076753311513163193766776549189437207405232814271648731913830979526841846195816158823957962550267437222093234138967941003160373458115111, 783576492029097084719143209491800987048409450822966308362590873596195259131721876168199925338938975425224987639741355215129116771727846366230011882068490884559883183717976291076026323720970452841498576474623562420355192949990568642899634356873617467114369756521220414836617599903, 1096730355809899825353756254499203842539523227587194506921650071458702062511060672493161267735755317915225950194598352388438827751762468035122024316080726805481346797672112873509068791054842420278654508569335049269043671776676570602649620147912659358959702274422128677999459880145, 257206254641538818431824803140673372962159089071222826519130579310647719945225003159349957782311506070099149282902924096244968232716365907561392650439466151625176257971059206131742187036778749931541555399501608053293333915835963902291781235247449888805906809659122358389669965901, 181091458444879260197129378855169836934375406113726021981382580987372920981422903917405210838967312556153283783631820117590745619937314017954293011397408737529430148777760721256707162949486582574312920603017762206339332593651040642489098000686889828197382170297810702662970158114, 320470192190562798795975334413238997928584246113060939505858039046063513234578991123627136887845332804078106596076580187387949419125894953466816383661807240824384882810365977162634879777667609260183437721658666296111843025333996211151794436913088647027540393824390862851530388400, 149354882382865005012111351535020069550349834739989955688100650562435974228968170714267212968260727816994184011430269118695536583744454798704675894412107245843048243899185829768525126569699350380665866491018343472939012946392460223045558252861123902104714582972094181869185080937, 560675576879607505483091170897029412625223855942058782723524471889301809854009529556601279567305633961176762713465878408265213945835328999978550049097988013952817039317127149446472676674799028654905066594305896496518483028019854381603618948291995116854890672084367319545080392549]

c = 6952100436236248545164162564638283221516621431609544056184328257688278966117749610107907505468485471534592919895367508409718136241405318745096373521149895160383024319179893706320570501334200713249625520485438249710450391489170081635880891161333259600001303283491897871583225335662

n, k = len(b), 20

#exploit

#leak r and then most of w due to bad q

r = 0
for i in b[:-k]:
    r = GCD(r, i)

w = [i // r for i in b[:-k]]

#brute force last k chars and normal decrypt rest

for i in product(range(2), repeat = k):
    cc = c
    for j in range(k):
        cc -= b[-k + j] * i[j]

    if cc % r == 0:
        cc //= r

        flg = [0] * (n - k) + list(i)
        for j in reversed(range(n - k)):
            flg[j] = cc // w[j]
            cc -= w[j] * flg[j] 

        flagbits = ''.join('0' if i == 0 else '1' for i in flg)

        try: 
            flag = int(flagbits, 2).to_bytes((n >> 3) + 1, 'big').decode('ascii') 
            print(flag)
        except:
            pass
