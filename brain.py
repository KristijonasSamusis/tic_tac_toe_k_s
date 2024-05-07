import random
import time


def ai(opponent, listas_check, brain_list, listas, symbol_x_o):
    """Opponent move decision-making function"""
    # Easy mode
    if opponent == "\033[95mPinky\033[0m":
        move = random.choice(listas_check)
        pinky_thinks = random.choice(
            ["Gee.. What to doo..", "Narf... I wish Brain was here..", "Pinky thinky..", "Zort!"])
        print(f"\n{opponent}: {pinky_thinks}")
        time.sleep(2)
        return str(move)

    # Bonus mode
    if opponent == "\033[92mPinky\033[0m":
        move = random.choice(listas_check)
        pinky_thinks = random.choice(
            ["Gee.. What to doo..", "Narf... I wish Brain was here..", "Pinky thinky..", "Zort!"])
        print(f"\n{opponent}: {pinky_thinks}")
        time.sleep(2)
        return str(move)

    # Mid mode:

    elif opponent == "\033[96mSnowball\033[0m":
        print("\n \033[96mSnowballing...\033[0m")
        priority_list = [5, 1, 7, 9, 3, 4, 8, 6, 2]

        if symbol_x_o == "\033[91mX\033[0m":
            symbol_opponent = "\033[34mO\033[0m"
        else:
            symbol_opponent = "\033[91mX\033[0m"
        # Possible rows
        horizontal_top = [listas[6], listas[7], listas[8]]
        horizontal_mid = [listas[3], listas[4], listas[5]]
        horizontal_bottom = [listas[0], listas[1], listas[2]]
        vertica_left = [listas[0], listas[3], listas[6]]
        vertica_mid = [listas[1], listas[4], listas[7]]
        vertica_right = [listas[2], listas[5], listas[8]]
        diagonally_right = [listas[6], listas[4], listas[2]]
        diagonally_left = [listas[0], listas[4], listas[8]]
        # Lists of possible rows
        row_options = [horizontal_bottom, horizontal_mid, horizontal_top, vertica_left, vertica_mid, vertica_right,
                       diagonally_right, diagonally_left]
        # Bone for priority lists of entry choice
        priority_1 = []
        priority_2 = []
        priority_3 = []
        priority_4 = []
        priority_5 = []
        priority_6 = []

        # sorting priorities by importance
        for rows in range(len(row_options)):
            empty_choices = [x_o for x_o in row_options[rows] if x_o != symbol_x_o]
            len_no_player = len(empty_choices)
            empty_choices_op = [x_o for x_o in row_options[rows] if x_o != symbol_opponent]
            len_no_opponent = len(empty_choices_op)
            if len_no_player == 1 and len_no_opponent == 3:
                priority_1.append(random.choice(empty_choices))
            elif len_no_opponent == 1 and len_no_player == 3:
                priority_2.append(random.choice(empty_choices_op))
            elif 5 in listas_check:
                priority_3.append(5)
            elif len_no_player == 2 and len_no_opponent == 3:
                for num in empty_choices:
                    if num in listas_check:
                        priority_4.append(num)
            else:
                for num in priority_list[1:5]:
                    if num in listas_check:
                        priority_5.append(num)
                for num2 in priority_list[5:]:
                    if num2 in listas_check:
                        priority_6.append(num2)

        while True:
            if len(priority_1) > 0:
                move = random.choice(priority_1)
                break
            elif len(priority_2) > 0:
                move = random.choice(priority_2)
                break
            elif len(priority_3) > 0:
                move = random.choice(priority_3)
                break
            elif len(priority_4) > 0:
                move = random.choice(priority_4)
                break
            elif len(priority_5) > 0:
                move = random.choice(priority_5)
                break
            elif len(priority_6) > 0:
                move = random.choice(priority_6)
                break
            else:
                move = random.choice(listas_check)
                break
        return str(move)


    # Hard mode
    elif opponent == "\033[93mThe Brain\033[0m":
        brain_thinks = random.choice(
            ["What am I doing here? I should be taking over the world!", "I’m surrounded by idiots.",
             "I am not a mice. I am a genius!", "Easy.", "This is nobrainer."])
        print(f"\n{opponent}: {brain_thinks}")
        match brain_list:
            case '':
                return random.choice(['5', '5', '5', '5', '5', '5', '1', '3', '7', '9'])

            case '54':
                return '1'
            case '5412' | '5413' | '5416' | '5417' | '5418':
                return '9'
            case '5419':
                return '3'
            case '541937':
                return '2'
            case '541932' | '541936' | '541938':
                return '7'

            case '52':
                return '3'
            case '5236' | '5239' | '5238' | '5231' | '5234':
                return '7'
            case '5237':
                return '9'
            case '523791':
                return '6'
            case '523796' | '523798' | '523794':
                return '1'

            case '56':
                return '9'
            case '5698' | '5697' | '5694' | '5693' | '5692':
                return '1'
            case '5691':
                return '7'
            case '569173':
                return '8'
            case '569178' | '569174' | '569172':
                return '3'

            case '58':
                return '7'
            case '5874' | '5871' | '5872' | '5879' | '5876':
                return '3'
            case '5873':
                return '1'
            case '587319':
                return '4'
            case '587314' | '587312' | '587316':
                return '9'

            case '51':
                return '9'
            case '5194':
                return '7'
            case '519472' | '519473' | '519476':
                return '8'
            case '519478':
                return '3'

            case '5192':
                return '3'
            case '519234' | '519237' | '519238':
                return '6'
            case '519236':
                return '7'

            case '5198':
                return '3'
            case '519837' | '519834' | '519832':
                return '6'
            case '519836':
                return '7'

            case '5196':
                return '7'
            case '519674' | '519672' | '519673':
                return '8'
            case '519678':
                return '3'

            case '53':
                return '7'
            case '5372':
                return '1'
            case '537216' | '537219' | '537218':
                return '4'
            case '537214':
                return '9'

            case '5376':
                return '9'
            case '537692' | '537691' | '537694':
                return '8'
            case '537698':
                return '1'

            case '5374':
                return '9'
            case '537491' | '537492' | '537496':
                return '8'
            case '537498':
                return '1'

            case '5378':
                return '1'
            case '537812' | '537816' | '537819':
                return '4'
            case '537814':
                return '9'

            case '59':
                return '1'
            case '5916':
                return '3'
            case '591638' | '591637' | '591634':
                return '2'
            case '591632':
                return '7'

            case '5918':
                return '7'
            case '591876' | '591873' | '591872':
                return '4'
            case '591874':
                return '3'

            case '5912':
                return '7'
            case '591273' | '591276' | '591278':
                return '4'
            case '591274':
                return '3'

            case '5914':
                return '3'
            case '591436' | '591438' | '591437':
                return '2'
            case '591432':
                return '7'

            case '57':
                return '3'
            case '5738':
                return '9'
            case '573894' | '573891' | '573892':
                return '6'
            case '573896':
                return '1'

            case '5734':
                return '1'
            case '573418' | '573419' | '573416':
                return '2'
            case '573412':
                return '9'

            case '5736':
                return '1'
            case '573619' | '573618' | '573614':
                return '2'
            case '573612':
                return '9'

            case '5732':
                return '9'
            case '573298' | '573294' | '573291':
                return '6'
            case '573296':
                return '1'

            case '51':
                return '9'
            case '5197':
                return '4'
            case '519748' | '519742' | '519743':
                return '6'
            case '519746':
                return '2'
            case '51974623':
                return '8'
            case '51974628':
                return '3'

            case '5193':
                return '2'
            case '519324' | '519327' | '519326':
                return '8'
            case '519328':
                return '4'
            case '51932847':
                return '6'
            case '51932846':
                return '7'

            case '53':
                return '7'
            case '5371':
                return '2'
            case '537124' | '537126' | '537129':
                return '8'
            case '537128':
                return '6'
            case '53712869':
                return '4'
            case '53712864':
                return '9'

            case '5379':
                return '6'
            case '537962' | '537961' | '537968':
                return '4'
            case '537964':
                return '2'
            case '53796421':
                return '8'
            case '53796428':
                return '1'

            case '59':
                return '1'
            case '5913':
                return '6'
            case '591362' | '591368' | '591367':
                return '4'
            case '591364':
                return '8'
            case '59136487':
                return '2'
            case '59136482':
                return '7'

            case '5917':
                return '8'
            case '591786' | '591783' | '591784':
                return '2'
            case '591782':
                return '6'
            case '59178263':
                return '4'
            case '59178264':
                return '3'

            case '57':
                return '3'
            case '5739':
                return '8'
            case '573986' | '573984' | '573981':
                return '2'
            case '573982':
                return '4'
            case '57398241':
                return '6'
            case '57398246':
                return '1'

            case '5731':
                return '4'
            case '573148' | '573149' | '573142':
                return '6'
            case '573146':
                return '8'
            case '57314689':
                return '2'
            case '57314682':
                return '9'
            # Player first / corners
            case '5':
                return '1'
            case '519':
                return '3'
            case '51934' | '51937' | '51938' | '51936':
                return '2'
            case '51932':
                return '8'
            case '5193287' | '5193284':
                return '6'
            case '5193286':
                return '4'

            case '517':
                return '3'
            case '51734' | '51738' | '51739' | '51736':
                return '2'
            case '51732':
                return '8'
            case '5173289' | '5173286':
                return '4'
            case '5173284':
                return '6'

            case '513':
                return '7'
            case '51378' | '51379' | '51376' | '51372':
                return '4'
            case '51374':
                return '6'
            case '5137468' | '5173289':
                return '2'
            case '5137462':
                return '8'

            case '5':
                return '3'
            case '537':
                return '9'
            case '53792' | '53791' | '53794' | '53798':
                return '6'
            case '53796':
                return '4'
            case '5379641' | '5379642':
                return '8'
            case '5379648':
                return '2'

            case '531':
                return '9'
            case '53192' | '53194' | '53197' | '53198':
                return '6'
            case '53196':
                return '4'
            case '5319647' | '5319648':
                return '2'
            case '5319642':
                return '8'

            case '539':
                return '1'
            case '53914' | '53917' | '53918' | '53916':
                return '2'
            case '53912':
                return '8'
            case '5391284' | '5319647':
                return '6'
            case '5391286':
                return '4'

            case '5':
                return '9'
            case '591':
                return '7'
            case '59176' | '59173' | '59172' | '59174':
                return '8'
            case '59178':
                return '2'
            case '5917823' | '5917826':
                return '4'
            case '5917824':
                return '6'

            case '593':
                return '7'
            case '59376' | '59372' | '59371' | '59374':
                return '8'
            case '59378':
                return '2'
            case '5937821' | '5937824':
                return '6'
            case '5937826':
                return '4'

            case '597':
                return '3'
            case '59732' | '59731' | '59734' | '59738':
                return '6'
            case '59736':
                return '4'
            case '5973642' | '5937821':
                return '8'
            case '5973648':
                return '2'

            case '5':
                return '7'
            case '573':
                return '1'
            case '57318' | '57319' | '57316' | '57312':
                return '4'
            case '57314':
                return '6'
            case '5731469' | '5731468':
                return '2'
            case '5731462':
                return '8'

            case '579':
                return '1'
            case '57918' | '57916' | '57913' | '57912':
                return '4'
            case '57914':
                return '6'
            case '5791463' | '5791462':
                return '8'
            case '5791468':
                return '2'

            case '571':
                return '9'
            case '57196' | '57193' | '57192' | '57194':
                return '8'
            case '57198':
                return '2'
            case '5719826' | '5791463':
                return '4'
            case '5719824':
                return '6'

            # Firs player center/side

            case '512':
                return '8'
            case '51284':
                return '6'
            case '5128469' | '5128463':
                return '7'
            case '5128467':
                return '3'

            case '51287':
                return '3'
            case '5128739' | '5128736':
                return '4'
            case '5128734':
                return '6'

            case '51286':
                return '4'
            case '5128649' | '5128643':
                return '7'
            case '5128647':
                return '3'

            case '51283':
                return '7'
            case '5128379' | '5128376':
                return '4'
            case '5128374':
                return '6'

            case '51289':
                return '4'
            case '5128946' | '5128943':
                return '7'
            case '5128947':
                return '3'

            case '514':
                return '6'
            case '51467':
                return '3'
            case '5146738' | '5146732':
                return '9'
            case '5146739':
                return '8'

            case '51468':
                return '2'
            case '5146827' | '5146829':
                return '3'
            case '5146823':
                return '7'

            case '51469':
                return '3'
            case '5146937' | '5146938':
                return '2'
            case '5146932':
                return '8'

            case '51463':
                return '7'
            case '5146378' | '5146379':
                return '2'
            case '5146372':
                return '8'

            case '51462':
                return '8'
            case '5146287' | '5146289':
                return '3'
            case '5146283':
                return '7'

            case '518':
                return '2'
            case '51824' | '51827' | '51826' | '51829':
                return '3'
            case '51823':
                return '7'
            case '5182379' | '5182376':
                return '4'
            case '5182374':
                return '6'

            case '516':
                return '4'
            case '51648' | '51649' | '51642' | '51643':
                return '7'
            case '51647':
                return '3'
            case '5164738' | '5164739':
                return '2'
            case '5164732':
                return '8'

            case '536':
                return '4'
            case '53642':
                return '8'
            case '5364287' | '5364289':
                return '1'
            case '5364281':
                return '9'

            case '53641':
                return '9'
            case '5364197' | '5364198':
                return '2'
            case '5364192':
                return '8'

            case '53648':
                return '2'
            case '5364827' | '5364829':
                return '1'
            case '5364821':
                return '9'

            case '53649':
                return '1'
            case '5364917' | '5364918':
                return '2'
            case '5364912':
                return '8'

            case '53647':
                return '2'
            case '5364728' | '5364729':
                return '1'
            case '5364721':
                return '9'

            case '532':
                return '8'
            case '53281':
                return '9'
            case '5328194' | '5328196':
                return '7'
            case '5328197':
                return '4'

            case '53284':
                return '6'
            case '5328461' | '5328467':
                return '9'
            case '5328469':
                return '1'

            case '53287':
                return '9'
            case '5328791' | '5328794':
                return '6'
            case '5328796':
                return '4'

            case '53289':
                return '1'
            case '5328914' | '5328917':
                return '6'
            case '5328916':
                return '4'

            case '53286':
                return '4'
            case '5328641' | '5328647':
                return '9'
            case '5328649':
                return '1'

            case '534':
                return '6'
            case '53462' | '53461' | '53468' | '53467':
                return '9'
            case '53469':
                return '1'
            case '5346917' | '5346918':
                return '2'
            case '5346912':
                return '8'

            case '538':
                return '2'
            case '53824' | '53827' | '53826' | '53829':
                return '1'
            case '53821':
                return '9'
            case '5382194' | '5382197':
                return '6'
            case '5382196':
                return '4'

            case '598':
                return '2'
            case '59826':
                return '4'
            case '5982641' | '5982647':
                return '3'
            case '5982643':
                return '7'

            case '59823':
                return '7'
            case '5982371' | '5982374':
                return '6'
            case '5982376':
                return '4'

            case '59824':
                return '6'
            case '5982461' | '5982467':
                return '3'
            case '5982463':
                return '7'

            case '59827':
                return '3'
            case '5982731' | '5982734':
                return '6'
            case '5982736':
                return '4'

            case '59821':
                return '6'
            case '5982164' | '5982167':
                return '3'
            case '5982163':
                return '7'

            case '596':
                return '4'
            case '59643':
                return '7'
            case '5964372' | '5964378':
                return '1'
            case '5964371':
                return '2'

            case '59642':
                return '8'
            case '5964283' | '5964281':
                return '7'
            case '5964287':
                return '3'

            case '59641':
                return '7'
            case '5964173' | '5964172':
                return '8'
            case '5964178':
                return '2'

            case '59647':
                return '3'
            case '5964732' | '5964731':
                return '8'
            case '5964738':
                return '2'

            case '59648':
                return '2'
            case '5964823' | '5964821':
                return '7'
            case '5964827':
                return '3'

            case '592':
                return '8'
            case '59286' | '59283' | '59284' | '59281':
                return '7'
            case '59287':
                return '3'
            case '5928731' | '5928734':
                return '6'
            case '5928736':
                return '4'

            case '594':
                return '6'
            case '59462' | '59461' | '59468' | '59467':
                return '3'
            case '59463':
                return '7'
            case '5946372' | '5946371':
                return '8'
            case '5946378':
                return '2'

            case '574':
                return '6'
            case '57468':
                return '2'
            case '5746823' | '5746821':
                return '9'
            case '5746829':
                return '1'

            case '57469':
                return '1'
            case '5746913' | '5746912':
                return '8'
            case '5746918':
                return '2'

            case '57462':
                return '8'
            case '5746283' | '5746281':
                return '9'
            case '5746289':
                return '1'

            case '57461':
                return '9'
            case '5746193' | '5746192':
                return '8'
            case '5746198':
                return '2'

            case '57463':
                return '8'
            case '5746382' | '5746381':
                return '9'
            case '5746389':
                return '1'

            case '578':
                return '2'
            case '57829':
                return '1'
            case '5782916' | '5782914':
                return '3'
            case '5782913':
                return '6'

            case '57826':
                return '4'
            case '5782649' | '5782643':
                return '1'
            case '5782641':
                return '9'

            case '57823':
                return '1'
            case '5782319' | '5782316':
                return '4'
            case '5782314':
                return '6'

            case '57821':
                return '9'
            case '5782196' | '5782193':
                return '4'
            case '5782194':
                return '6'

            case '57824':
                return '6'
            case '5782469' | '5782463':
                return '1'
            case '5782461':
                return '9'

            case '576':
                return '4'
            case '57648' | '57649' | '57642' | '57643':
                return '1'
            case '57641':
                return '9'
            case '5764193' | '5764192':
                return '8'
            case '5764198':
                return '2'

            case '572':
                return '8'
            case '57286' | '57283' | '57284' | '57281':
                return '9'
            case '57289':
                return '1'
            case '5728916' | '5728913':
                return '4'
            case '5728914':
                return '6'
            # First layer corner

            case '1':
                return '5'
            case '154':
                return '7'
            case '15478' | '15479' | '15476' | '15472':
                return '3'
            case '15473':
                return '2'
            case '1547329' | '1547326':
                return '8'
            case '1547328':
                return '6'

            case '157':
                return '4'
            case '15748' | '15749' | '15742' | '15743':
                return '6'
            case '15746':
                return '2'
            case '1574629' | '1574623':
                return '8'
            case '1574628':
                return '9'

            case '159':
                return '6'
            case '15967' | '15968' | '15962' | '15963':
                return '4'
            case '15964':
                return '7'
            case '1596478' | '1596472':
                return '3'
            case '1596473':
                return '2'

            case '153':
                return '2'
            case '15324' | '15327' | '15329' | '15326':
                return '8'
            case '15328':
                return '4'
            case '1532847' | '1532849':
                return '6'
            case '1532846':
                return '9'

            case '152':
                return '3'
            case '15234' | '15238' | '15239' | '15236':
                return '7'
            case '15237':
                return '4'
            case '1523748' | '1523749':
                return '6'
            case '1523746':
                return '8'

            case '158':
                return '9'
            case '15892':
                return '3'
            case '1589237' | '1589234':
                return '6'
            case '1589236':
                return '7'
            case '15894':
                return '7'
            case '1589472' | '1589476':
                return '3'
            case '1589473':
                return '2'

            case '15897':
                return '4'
            case '1589742' | '1589743':
                return '6'
            case '1589746':
                return '2'

            case '15896':
                return '3'
            case '1589634' | '1589632':
                return '7'
            case '1589637':
                return '4'

            case '15893':
                return '2'
            case '1589327' | '1589326':
                return '4'
            case '1589324':
                return '7'

            case '156':
                return '9'
            case '15694':
                return '7'
            case '1569472' | '1569473':
                return '8'
            case '1569478':
                return '3'
            case '1567':
                return '4'
            case '156748' | '156742':
                return '3'
            case '156743':
                return '2'

            case '15698':
                return '7'
            case '1569874' | '1569872':
                return '3'
            case '1569873':
                return '2'

            case '15693':
                return '2'
            case '1569324' | '1569327':
                return '8'
            case '1569328':
                return '4'

            case '15692':
                return '3'
            case '1569234' | '1569238':
                return '7'
            case '1569237':
                return '4'

            case '3':
                return '5'
            case '352':
                return '1'
            case '35214' | '35217' | '35218' | '35216':
                return '9'
            case '35219':
                return '6'
            case '3521967' | '3521968':
                return '4'
            case '3521964':
                return '8'

            case '351':
                return '2'
            case '35124' | '35127' | '35126' | '35129':
                return '8'
            case '35128':
                return '6'
            case '3512867' | '3512869':
                return '4'
            case '3512864':
                return '7'

            case '357':
                return '8'
            case '35781' | '35784' | '35786' | '35789':
                return '2'
            case '35782':
                return '1'
            case '3578214' | '3578216':
                return '9'
            case '3578219':
                return '6'

            case '359':
                return '6'
            case '35962' | '35961' | '35967' | '35968':
                return '4'
            case '35964':
                return '2'
            case '3596421' | '3596427':
                return '8'
            case '3596428':
                return '7'

            case '356':
                return '9'
            case '35692' | '35694' | '35697' | '35698':
                return '1'
            case '35691':
                return '2'
            case '3569124' | '3569127':
                return '8'
            case '3569128':
                return '4'

            case '354':
                return '7'
            case '35476':
                return '9'
            case '3547691' | '3547692':
                return '8'
            case '3547698':
                return '1'
            case '35472':
                return '1'
            case '3547216' | '3547218':
                return '9'
            case '3547219':
                return '6'

            case '35471':
                return '2'
            case '3547126' | '3547129':
                return '8'
            case '3547128':
                return '6'

            case '35478':
                return '9'
            case '3547892' | '3547896':
                return '1'
            case '3547891':
                return '2'

            case '35479':
                return '6'
            case '3547961' | '3547968':
                return '2'
            case '3547962':
                return '1'

            case '358':
                return '7'
            case '35872':
                return '1'
            case '3587216' | '3587219':
                return '4'
            case '3587214':
                return '9'
            case '3581':
                return '2'
            case '358124' | '358126':
                return '9'
            case '358129':
                return '6'

            case '35874':
                return '1'
            case '3587412' | '3587416':
                return '9'
            case '3587419':
                return '6'

            case '35879':
                return '6'
            case '3587962' | '3587961':
                return '4'
            case '3587964':
                return '2'

            case '35876':
                return '9'
            case '3587692' | '3587694':
                return '1'
            case '3587691':
                return '2'

            case '9':
                return '5'
            case '956':
                return '3'
            case '95632' | '95631' | '95634' | '95638':
                return '7'
            case '95637':
                return '8'
            case '9563781' | '9563784':
                return '2'
            case '9563782':
                return '4'

            case '953':
                return '6'
            case '95362' | '95361' | '95368' | '95367':
                return '4'
            case '95364':
                return '8'
            case '9536481' | '9536487':
                return '2'
            case '9536482':
                return '1'

            case '951':
                return '4'
            case '95143' | '95142' | '95148' | '95147':
                return '6'
            case '95146':
                return '3'
            case '9514632' | '9514638':
                return '7'
            case '9514637':
                return '8'

            case '957':
                return '8'
            case '95786' | '95783' | '95781' | '95784':
                return '2'
            case '95782':
                return '6'
            case '9578263' | '9578261':
                return '4'
            case '9578264':
                return '1'

            case '958':
                return '7'
            case '95876' | '95872' | '95871' | '95874':
                return '3'
            case '95873':
                return '6'
            case '9587362' | '9587361':
                return '4'
            case '9587364':
                return '2'

            case '952':
                return '1'
            case '95218':
                return '7'
            case '9521873' | '9521876':
                return '4'
            case '9521874':
                return '3'
            case '95216':
                return '3'
            case '9521638' | '9521634':
                return '7'
            case '9521637':
                return '8'

            case '95213':
                return '6'
            case '9521368' | '9521367':
                return '4'
            case '9521364':
                return '8'

            case '95214':
                return '7'
            case '9521476' | '9521478':
                return '3'
            case '9521473':
                return '6'

            case '95217':
                return '8'
            case '9521783' | '9521784':
                return '6'
            case '9521786':
                return '3'

            case '954':
                return '1'
            case '95416':
                return '3'
            case '9541638' | '9541637':
                return '2'
            case '9541632':
                return '7'
            case '9543':
                return '6'
            case '954362' | '954368':
                return '7'
            case '954367':
                return '8'

            case '95412':
                return '3'
            case '9541236' | '9541238':
                return '7'
            case '9541237':
                return '8'

            case '95417':
                return '8'
            case '9541786' | '9541783':
                return '2'
            case '9541782':
                return '6'

            case '95418':
                return '7'
            case '9541876' | '9541872':
                return '3'
            case '9541873':
                return '6'

            case '7':
                return '5'
            case '758':
                return '9'
            case '75896' | '75893' | '75892' | '75894':
                return '1'
            case '75891':
                return '4'
            case '7589143' | '7589142':
                return '6'
            case '7589146':
                return '2'

            case '759':
                return '8'
            case '75986' | '75983' | '75984' | '75981':
                return '2'
            case '75982':
                return '4'
            case '7598243' | '7598241':
                return '6'
            case '7598246':
                return '3'

            case '753':
                return '2'
            case '75329' | '75326' | '75324' | '75321':
                return '8'
            case '75328':
                return '9'
            case '7532896' | '7532894':
                return '1'
            case '7532891':
                return '4'

            case '751':
                return '4'
            case '75148' | '75149' | '75143' | '75142':
                return '6'
            case '75146':
                return '8'
            case '7514689' | '7514683':
                return '2'
            case '7514682':
                return '3'

            case '754':
                return '1'
            case '75418' | '75416' | '75413' | '75412':
                return '9'
            case '75419':
                return '8'
            case '7541986' | '7541983':
                return '2'
            case '7541982':
                return '6'

            case '756':
                return '3'
            case '75634':
                return '1'
            case '7563419' | '7563418':
                return '2'
            case '7563412':
                return '9'
            case '75638':
                return '9'
            case '7563894' | '7563892':
                return '1'
            case '7563891':
                return '4'

            case '75639':
                return '8'
            case '7563984' | '7563981':
                return '2'
            case '7563982':
                return '4'

            case '75632':
                return '1'
            case '7563218' | '7563214':
                return '9'
            case '7563219':
                return '8'

            case '75631':
                return '4'
            case '7563149' | '7563142':
                return '8'
            case '7563148':
                return '9'

            case '752':
                return '3'
            case '75238':
                return '9'
            case '7523894' | '7523891':
                return '6'
            case '7523896':
                return '1'
            case '7529':
                return '8'
            case '752986' | '752984':
                return '1'
            case '752981':
                return '4'

            case '75236':
                return '9'
            case '7523698' | '7523694':
                return '1'
            case '7523691':
                return '4'

            case '75231':
                return '4'
            case '7523148' | '7523149':
                return '6'
            case '7523146':
                return '8'

            case '75234':
                return '1'
            case '7523418' | '7523416':
                return '9'
            case '7523419':
                return '8'
            # First player side
            case '4':
                return '5'
            case '457':
                return '1'
            case '45718' | '45712' | '45713' | '45716':
                return '9'
            case '45719':
                return '8'
            case '4571986' | '4571983':
                return '2'
            case '4571982':
                return '3'

            case '458':
                return '7'
            case '45871' | '45872' | '45879' | '45876':
                return '3'
            case '45873':
                return '1'
            case '4587312' | '4587316':
                return '9'
            case '4587319':
                return '6'

            case '459':
                return '7'
            case '45978' | '45976' | '45971' | '45972':
                return '3'
            case '45973':
                return '6'
            case '4597368' | '4597362':
                return '1'
            case '4597361':
                return '2'

            case '453':
                return '2'
            case '45321' | '45327' | '45329' | '45326':
                return '8'
            case '45328':
                return '9'
            case '4532897' | '4532896':
                return '1'
            case '4532891':
                return '7'

            case '452':
                return '1'
            case '45217' | '45218' | '45216' | '45213':
                return '9'
            case '45219':
                return '7'
            case '4521978' | '4521978':
                return '3'
            case '4521973':
                return '6'

            case '451':
                return '7'
            case '45178' | '45179' | '45176' | '45172':
                return '3'
            case '45173':
                return '2'
            case '4517329' | '4517326':
                return '8'
            case '4517328':
                return '9'

            case '456':
                return '1'
            case '45617' | '45618' | '45612' | '45613':
                return '9'
            case '45619':
                return '3'
            case '4561937' | '4561938':
                return '2'
            case '4561932':
                return '7'

            case '2':
                return '5'
            case '251':
                return '3'
            case '25134' | '25136' | '25139' | '25138':
                return '7'
            case '25137':
                return '4'
            case '2513748' | '2513749':
                return '6'
            case '2513746':
                return '9'

            case '254':
                return '1'
            case '25413' | '25416' | '25417' | '25418':
                return '9'
            case '25419':
                return '3'
            case '2541936' | '2541938':
                return '7'
            case '2541937':
                return '8'

            case '257':
                return '1'
            case '25714' | '25718' | '25713' | '25716':
                return '9'
            case '25719':
                return '8'
            case '2571984' | '2571986':
                return '3'
            case '2571983':
                return '6'

            case '259':
                return '6'
            case '25963' | '25961' | '25967' | '25968':
                return '4'
            case '25964':
                return '7'
            case '2596471' | '2596478':
                return '3'
            case '2596473':
                return '1'

            case '256':
                return '3'
            case '25631' | '25634' | '25638' | '25639':
                return '7'
            case '25637':
                return '1'
            case '2563714' | '2563714':
                return '9'
            case '2563719':
                return '8'

            case '253':
                return '1'
            case '25314' | '25317' | '25318' | '25316':
                return '9'
            case '25319':
                return '6'
            case '2531967' | '2531968':
                return '4'
            case '2531964':
                return '7'

            case '258':
                return '3'
            case '25831' | '25834' | '25836' | '25839':
                return '7'
            case '25837':
                return '9'
            case '2583791' | '2583794':
                return '6'
            case '2583796':
                return '1'

            case '6':
                return '5'
            case '653':
                return '9'
            case '65392' | '65398' | '65397' | '65394':
                return '1'
            case '65391':
                return '2'
            case '6539124' | '6539127':
                return '8'
            case '6539128':
                return '7'

            case '652':
                return '3'
            case '65239' | '65238' | '65231' | '65234':
                return '7'
            case '65237':
                return '9'
            case '6523798' | '6523794':
                return '1'
            case '6523791':
                return '4'

            case '651':
                return '3'
            case '65132' | '65134' | '65139' | '65138':
                return '7'
            case '65137':
                return '4'
            case '6513742' | '6513748':
                return '9'
            case '6513749':
                return '8'

            case '657':
                return '8'
            case '65789' | '65783' | '65781' | '65784':
                return '2'
            case '65782':
                return '1'
            case '6578213' | '6578214':
                return '9'
            case '6578219':
                return '3'

            case '658':
                return '9'
            case '65893' | '65892' | '65894' | '65897':
                return '1'
            case '65891':
                return '3'
            case '6589132' | '6589132':
                return '7'
            case '6589137':
                return '4'

            case '659':
                return '3'
            case '65932' | '65931' | '65934' | '65938':
                return '7'
            case '65937':
                return '8'
            case '6593781' | '6593784':
                return '2'
            case '6593782':
                return '1'

            case '654':
                return '9'
            case '65493' | '65492' | '65498' | '65497':
                return '1'
            case '65491':
                return '7'
            case '6549173' | '6549172':
                return '8'
            case '6549178':
                return '3'

            case '8':
                return '5'
            case '859':
                return '7'
            case '85976' | '85974' | '85971' | '85972':
                return '3'
            case '85973':
                return '6'
            case '8597362' | '8597361':
                return '4'
            case '8597364':
                return '1'

            case '856':
                return '9'
            case '85697' | '85694' | '85693' | '85692':
                return '1'
            case '85691':
                return '7'
            case '8569174' | '8569172':
                return '3'
            case '8569173':
                return '2'

            case '853':
                return '9'
            case '85396' | '85392' | '85397' | '85394':
                return '1'
            case '85391':
                return '2'
            case '8539126' | '8539124':
                return '7'
            case '8539127':
                return '4'

            case '851':
                return '4'
            case '85147' | '85149' | '85143' | '85142':
                return '6'
            case '85146':
                return '3'
            case '8514639' | '8514632':
                return '7'
            case '8514637':
                return '9'

            case '854':
                return '7'
            case '85479' | '85476' | '85472' | '85471':
                return '3'
            case '85473':
                return '9'
            case '8547396' | '8547396':
                return '1'
            case '8547391':
                return '2'

            case '857':
                return '9'
            case '85796' | '85793' | '85792' | '85794':
                return '1'
            case '85791':
                return '4'
            case '8579143' | '8579142':
                return '6'
            case '8579146':
                return '3'

            case '852':
                return '7'
            case '85279' | '85276' | '85274' | '85271':
                return '3'
            case '85273':
                return '1'
            case '8527319' | '8527316':
                return '4'
            case '8527314':
                return '9'
            # Brain first, corner.

            case '14':
                return '5'
            case '1457' | '1458' | '1452' | '1453' | '1456':
                return '9'
            case '1459':
                return '3'
            case '145937' | '145938' | '145936':
                return '2'
            case '145932':
                return '7'

            case '17':
                return '3'
            case '1738' | '1739' | '1734' | '1735' | '1736':
                return '2'
            case '1732':
                return '9'
            case '173294' | '173295' | '173298':
                return '6'
            case '173296':
                return '5'

            case '18':
                return '5'
            case '1857' | '1854' | '1852' | '1853' | '1856':
                return '9'
            case '1859':
                return '7'
            case '185972' | '185976' | '185973':
                return '4'
            case '185974':
                return '3'

            case '19':
                return '7'
            case '1978' | '1975' | '1972' | '1976' | '1973':
                return '4'
            case '1974':
                return '3'
            case '197438' | '197435' | '197436':
                return '2'
            case '197432':
                return '5'

            case '16':
                return '5'
            case '1654' | '1657' | '1658' | '1652' | '1653':
                return '9'
            case '1659':
                return '3'
            case '165934' | '165937' | '165938':
                return '2'
            case '165932':
                return '7'

            case '13':
                return '7'
            case '1372' | '1375' | '1378' | '1379' | '1376':
                return '4'
            case '1374':
                return '9'
            case '137492' | '137495' | '137496':
                return '8'
            case '137498':
                return '5'

            case '12':
                return '5'
            case '1254' | '1257' | '1258' | '1256' | '1253':
                return '9'
            case '1259':
                return '7'
            case '125978' | '125976' | '125973':
                return '4'
            case '125974':
                return '3'

            case '15':
                return '9'
            case '1594':
                return '6'
            case '15946':
                return ''
            case '159467' | '159468' | '159462':
                return '3'
            case '159463':
                return '7'
            case '15946372':
                return '8'
            case '15946378':
                return '2'

            case '1598':
                return '2'
            case '159824' | '159827' | '159826':
                return '3'
            case '159823':
                return '7'
            case '15982374':
                return '6'
            case '15982376':
                return '4'

            case '1596':
                return '4'
            case '159648' | '159642' | '159643':
                return '7'
            case '159647':
                return '3'
            case '15964738':
                return '2'
            case '15964732':
                return '8'

            case '1592':
                return '8'
            case '159284' | '159286' | '159283':
                return '7'
            case '159287':
                return '3'
            case '15928734':
                return '6'
            case '15928736':
                return '4'

            case '1597':
                return '3'
            case '159734' | '159738' | '159736':
                return '2'
            case '159732':
                return '6'

            case '1593':
                return '7'
            case '159374' | '159372' | '159376':
                return '8'
            case '159378':
                return '4'

            case '32':
                return '5'
            case '3251' | '3254' | '3256' | '3259' | '3258':
                return '7'
            case '3257':
                return '9'
            case '325791' | '325794' | '325798':
                return '6'
            case '325796':
                return '1'

            case '31':
                return '9'
            case '3194' | '3197' | '3192' | '3195' | '3198':
                return '6'
            case '3196':
                return '7'
            case '319672' | '319675' | '319674':
                return '8'
            case '319678':
                return '5'

            case '34':
                return '5'
            case '3451' | '3452' | '3456' | '3459' | '3458':
                return '7'
            case '3457':
                return '1'
            case '345716' | '345718' | '345719':
                return '2'
            case '345712':
                return '9'

            case '37':
                return '1'
            case '3714' | '3715' | '3716' | '3718' | '3719':
                return '2'
            case '3712':
                return '9'
            case '371294' | '371295' | '371298':
                return '6'
            case '371296':
                return '5'

            case '38':
                return '5'
            case '3852' | '3851' | '3854' | '3856' | '3859':
                return '7'
            case '3857':
                return '9'
            case '385792' | '385791' | '385794':
                return '6'
            case '385796':
                return '1'

            case '39':
                return '1'
            case '3916' | '3915' | '3914' | '3917' | '3918':
                return '2'
            case '3912':
                return '7'
            case '391276' | '391275' | '391278':
                return '4'
            case '391274':
                return '5'

            case '36':
                return '5'
            case '3652' | '3651' | '3654' | '3658' | '3659':
                return '7'
            case '3657':
                return '1'
            case '365714' | '365718' | '365719':
                return '2'
            case '365712':
                return '9'

            case '35':
                return '7'
            case '3572':
                return '8'
            case '35728':
                return ''
            case '357281' | '357284' | '357286':
                return '9'
            case '357289':
                return '1'
            case '35728916':
                return '4'
            case '35728914':
                return '6'

            case '3574':
                return '6'
            case '357462' | '357461' | '357468':
                return '9'
            case '357469':
                return '1'
            case '35746912':
                return '8'
            case '35746918':
                return '2'

            case '3578':
                return '2'
            case '357824' | '357826' | '357829':
                return '1'
            case '357821':
                return '9'
            case '35782194':
                return '6'
            case '35782196':
                return '4'

            case '3576':
                return '4'
            case '357642' | '357648' | '357649':
                return '1'
            case '357641':
                return '9'
            case '35764192':
                return '8'
            case '35764198':
                return '2'

            case '3571':
                return '9'
            case '357192' | '357194' | '357198':
                return '6'
            case '357196':
                return '8'

            case '3579':
                return '1'
            case '357912' | '357916' | '357918':
                return '4'
            case '357914':
                return '2'

            case '96':
                return '5'
            case '9653' | '9652' | '9658' | '9657' | '9654':
                return '1'
            case '9651':
                return '7'
            case '965173' | '965172' | '965174':
                return '8'
            case '965178':
                return '3'

            case '93':
                return '7'
            case '9372' | '9371' | '9376' | '9375' | '9374':
                return '8'
            case '9378':
                return '1'
            case '937816' | '937815' | '937812':
                return '4'
            case '937814':
                return '5'

            case '92':
                return '5'
            case '9253' | '9256' | '9258' | '9257' | '9254':
                return '1'
            case '9251':
                return '3'
            case '925138' | '925134' | '925137':
                return '6'
            case '925136':
                return '7'

            case '91':
                return '3'
            case '9132' | '9135' | '9138' | '9134' | '9137':
                return '6'
            case '9136':
                return '7'
            case '913672' | '913675' | '913674':
                return '8'
            case '913678':
                return '5'

            case '94':
                return '5'
            case '9456' | '9453' | '9452' | '9458' | '9457':
                return '1'
            case '9451':
                return '7'
            case '945176' | '945173' | '945172':
                return '8'
            case '945178':
                return '3'

            case '97':
                return '3'
            case '9738' | '9735' | '9732' | '9731' | '9734':
                return '6'
            case '9736':
                return '1'
            case '973618' | '973615' | '973614':
                return '2'
            case '973612':
                return '5'

            case '98':
                return '5'
            case '9856' | '9853' | '9852' | '9854' | '9857':
                return '1'
            case '9851':
                return '3'
            case '985132' | '985134' | '985137':
                return '6'
            case '985136':
                return '7'

            case '95':
                return '1'
            case '9516':
                return '4'
            case '95164':
                return ''
            case '951643' | '951642' | '951648':
                return '7'
            case '951647':
                return '3'
            case '95164738':
                return '2'
            case '95164732':
                return '8'

            case '9512':
                return '8'
            case '951286' | '951283' | '951284':
                return '7'
            case '951287':
                return '3'
            case '95128736':
                return '4'
            case '95128734':
                return '6'

            case '9514':
                return '6'
            case '951462' | '951468' | '951467':
                return '3'
            case '951463':
                return '7'
            case '95146372':
                return '8'
            case '95146378':
                return '2'

            case '9518':
                return '2'
            case '951826' | '951824' | '951827':
                return '3'
            case '951823':
                return '7'
            case '95182376':
                return '4'
            case '95182374':
                return '6'

            case '9513':
                return '7'
            case '951376' | '951372' | '951374':
                return '8'
            case '951378':
                return '4'

            case '9517':
                return '3'
            case '951736' | '951738' | '951734':
                return '2'
            case '951732':
                return '6'

            case '78':
                return '5'
            case '7859' | '7856' | '7854' | '7851' | '7852':
                return '3'
            case '7853':
                return '1'
            case '785319' | '785316' | '785312':
                return '4'
            case '785314':
                return '9'

            case '79':
                return '1'
            case '7916' | '7913' | '7918' | '7915' | '7912':
                return '4'
            case '7914':
                return '3'
            case '791438' | '791435' | '791436':
                return '2'
            case '791432':
                return '5'

            case '76':
                return '5'
            case '7659' | '7658' | '7654' | '7651' | '7652':
                return '3'
            case '7653':
                return '9'
            case '765394' | '765392' | '765391':
                return '8'
            case '765398':
                return '1'

            case '73':
                return '9'
            case '7396' | '7395' | '7394' | '7392' | '7391':
                return '8'
            case '7398':
                return '1'
            case '739816' | '739815' | '739812':
                return '4'
            case '739814':
                return '5'

            case '72':
                return '5'
            case '7258' | '7259' | '7256' | '7254' | '7251':
                return '3'
            case '7253':
                return '1'
            case '725318' | '725319' | '725316':
                return '4'
            case '725314':
                return '9'

            case '71':
                return '9'
            case '7194' | '7195' | '7196' | '7193' | '7192':
                return '8'
            case '7198':
                return '3'
            case '719834' | '719835' | '719832':
                return '6'
            case '719836':
                return '5'

            case '74':
                return '5'
            case '7458' | '7459' | '7456' | '7452' | '7451':
                return '3'
            case '7453':
                return '9'
            case '745396' | '745392' | '745391':
                return '8'
            case '745398':
                return '1'

            case '75':
                return '3'
            case '7538':
                return '2'
            case '75382':
                return ''
            case '753829' | '753826' | '753824':
                return '1'
            case '753821':
                return '9'
            case '75382194':
                return '6'
            case '75382196':
                return '4'

            case '7536':
                return '4'
            case '753648' | '753649' | '753642':
                return '1'
            case '753641':
                return '9'
            case '75364198':
                return '2'
            case '75364192':
                return '8'

            case '7532':
                return '8'
            case '753286' | '753284' | '753281':
                return '9'
            case '753289':
                return '1'
            case '75328916':
                return '4'
            case '75328914':
                return '6'

            case '7534':
                return '6'
            case '753468' | '753462' | '753461':
                return '9'
            case '753469':
                return '1'
            case '75346918':
                return '2'
            case '75346912':
                return '8'

            case '7539':
                return '1'
            case '753918' | '753916' | '753912':
                return '4'
            case '753914':
                return '2'

            case '7531':
                return '9'
            case '753198' | '753194' | '753192':
                return '6'
            case '753196':
                return '8'
            case '14':
                return '5'
            case '1457' | '1458' | '1452' | '1453' | '1456':
                return '9'
            case '1459':
                return '3'
            case '145937' | '145938' | '145936':
                return '2'
            case '145932':
                return '7'

            case '17':
                return '3'
            case '1738' | '1739' | '1734' | '1735' | '1736':
                return '2'
            case '1732':
                return '9'
            case '173294' | '173295' | '173298':
                return '6'
            case '173296':
                return '5'

            case '18':
                return '5'
            case '1857' | '1854' | '1852' | '1853' | '1856':
                return '9'
            case '1859':
                return '7'
            case '185972' | '185976' | '185973':
                return '4'
            case '185974':
                return '3'

            case '19':
                return '7'
            case '1978' | '1975' | '1972' | '1976' | '1973':
                return '4'
            case '1974':
                return '3'
            case '197438' | '197435' | '197436':
                return '2'
            case '197432':
                return '5'

            case '16':
                return '5'
            case '1654' | '1657' | '1658' | '1652' | '1653':
                return '9'
            case '1659':
                return '3'
            case '165934' | '165937' | '165938':
                return '2'
            case '165932':
                return '7'

            case '13':
                return '7'
            case '1372' | '1375' | '1378' | '1379' | '1376':
                return '4'
            case '1374':
                return '9'
            case '137492' | '137495' | '137496':
                return '8'
            case '137498':
                return '5'

            case '12':
                return '5'
            case '1254' | '1257' | '1258' | '1256' | '1253':
                return '9'
            case '1259':
                return '7'
            case '125978' | '125976' | '125973':
                return '4'
            case '125974':
                return '3'

            case '15':
                return '9'
            case '1594':
                return '6'
            case '15946':
                return ''
            case '159467' | '159468' | '159462':
                return '3'
            case '159463':
                return '7'
            case '15946372':
                return '8'
            case '15946378':
                return '2'

            case '1598':
                return '2'
            case '159824' | '159827' | '159826':
                return '3'
            case '159823':
                return '7'
            case '15982374':
                return '6'
            case '15982376':
                return '4'

            case '1596':
                return '4'
            case '159648' | '159642' | '159643':
                return '7'
            case '159647':
                return '3'
            case '15964738':
                return '2'
            case '15964732':
                return '8'

            case '1592':
                return '8'
            case '159284' | '159286' | '159283':
                return '7'
            case '159287':
                return '3'
            case '15928734':
                return '6'
            case '15928736':
                return '4'

            case '1597':
                return '3'
            case '159734' | '159738' | '159736':
                return '2'
            case '159732':
                return '6'

            case '1593':
                return '7'
            case '159374' | '159372' | '159376':
                return '8'
            case '159378':
                return '4'

            case '32':
                return '5'
            case '3251' | '3254' | '3256' | '3259' | '3258':
                return '7'
            case '3257':
                return '9'
            case '325791' | '325794' | '325798':
                return '6'
            case '325796':
                return '1'

            case '31':
                return '9'
            case '3194' | '3197' | '3192' | '3195' | '3198':
                return '6'
            case '3196':
                return '7'
            case '319672' | '319675' | '319674':
                return '8'
            case '319678':
                return '5'

            case '34':
                return '5'
            case '3451' | '3452' | '3456' | '3459' | '3458':
                return '7'
            case '3457':
                return '1'
            case '345716' | '345718' | '345719':
                return '2'
            case '345712':
                return '9'

            case '37':
                return '1'
            case '3714' | '3715' | '3716' | '3718' | '3719':
                return '2'
            case '3712':
                return '9'
            case '371294' | '371295' | '371298':
                return '6'
            case '371296':
                return '5'

            case '38':
                return '5'
            case '3852' | '3851' | '3854' | '3856' | '3859':
                return '7'
            case '3857':
                return '9'
            case '385792' | '385791' | '385794':
                return '6'
            case '385796':
                return '1'

            case '39':
                return '1'
            case '3916' | '3915' | '3914' | '3917' | '3918':
                return '2'
            case '3912':
                return '7'
            case '391276' | '391275' | '391278':
                return '4'
            case '391274':
                return '5'

            case '36':
                return '5'
            case '3652' | '3651' | '3654' | '3658' | '3659':
                return '7'
            case '3657':
                return '1'
            case '365714' | '365718' | '365719':
                return '2'
            case '365712':
                return '9'

            case '35':
                return '7'
            case '3572':
                return '8'
            case '35728':
                return ''
            case '357281' | '357284' | '357286':
                return '9'
            case '357289':
                return '1'
            case '35728916':
                return '4'
            case '35728914':
                return '6'

            case '3574':
                return '6'
            case '357462' | '357461' | '357468':
                return '9'
            case '357469':
                return '1'
            case '35746912':
                return '8'
            case '35746918':
                return '2'

            case '3578':
                return '2'
            case '357824' | '357826' | '357829':
                return '1'
            case '357821':
                return '9'
            case '35782194':
                return '6'
            case '35782196':
                return '4'

            case '3576':
                return '4'
            case '357642' | '357648' | '357649':
                return '1'
            case '357641':
                return '9'
            case '35764192':
                return '8'
            case '35764198':
                return '2'

            case '3571':
                return '9'
            case '357192' | '357194' | '357198':
                return '6'
            case '357196':
                return '8'

            case '3579':
                return '1'
            case '357912' | '357916' | '357918':
                return '4'
            case '357914':
                return '2'

            case '96':
                return '5'
            case '9653' | '9652' | '9658' | '9657' | '9654':
                return '1'
            case '9651':
                return '7'
            case '965173' | '965172' | '965174':
                return '8'
            case '965178':
                return '3'

            case '93':
                return '7'
            case '9372' | '9371' | '9376' | '9375' | '9374':
                return '8'
            case '9378':
                return '1'
            case '937816' | '937815' | '937812':
                return '4'
            case '937814':
                return '5'

            case '92':
                return '5'
            case '9253' | '9256' | '9258' | '9257' | '9254':
                return '1'
            case '9251':
                return '3'
            case '925138' | '925134' | '925137':
                return '6'
            case '925136':
                return '7'

            case '91':
                return '3'
            case '9132' | '9135' | '9138' | '9134' | '9137':
                return '6'
            case '9136':
                return '7'
            case '913672' | '913675' | '913674':
                return '8'
            case '913678':
                return '5'

            case '94':
                return '5'
            case '9456' | '9453' | '9452' | '9458' | '9457':
                return '1'
            case '9451':
                return '7'
            case '945176' | '945173' | '945172':
                return '8'
            case '945178':
                return '3'

            case '97':
                return '3'
            case '9738' | '9735' | '9732' | '9731' | '9734':
                return '6'
            case '9736':
                return '1'
            case '973618' | '973615' | '973614':
                return '2'
            case '973612':
                return '5'

            case '98':
                return '5'
            case '9856' | '9853' | '9852' | '9854' | '9857':
                return '1'
            case '9851':
                return '3'
            case '985132' | '985134' | '985137':
                return '6'
            case '985136':
                return '7'

            case '95':
                return '1'
            case '9516':
                return '4'
            case '95164':
                return ''
            case '951643' | '951642' | '951648':
                return '7'
            case '951647':
                return '3'
            case '95164738':
                return '2'
            case '95164732':
                return '8'

            case '9512':
                return '8'
            case '951286' | '951283' | '951284':
                return '7'
            case '951287':
                return '3'
            case '95128736':
                return '4'
            case '95128734':
                return '6'

            case '9514':
                return '6'
            case '951462' | '951468' | '951467':
                return '3'
            case '951463':
                return '7'
            case '95146372':
                return '8'
            case '95146378':
                return '2'

            case '9518':
                return '2'
            case '951826' | '951824' | '951827':
                return '3'
            case '951823':
                return '7'
            case '95182376':
                return '4'
            case '95182374':
                return '6'

            case '9513':
                return '7'
            case '951376' | '951372' | '951374':
                return '8'
            case '951378':
                return '4'

            case '9517':
                return '3'
            case '951736' | '951738' | '951734':
                return '2'
            case '951732':
                return '6'

            case '78':
                return '5'
            case '7859' | '7856' | '7854' | '7851' | '7852':
                return '3'
            case '7853':
                return '1'
            case '785319' | '785316' | '785312':
                return '4'
            case '785314':
                return '9'

            case '79':
                return '1'
            case '7916' | '7913' | '7918' | '7915' | '7912':
                return '4'
            case '7914':
                return '3'
            case '791438' | '791435' | '791436':
                return '2'
            case '791432':
                return '5'

            case '76':
                return '5'
            case '7659' | '7658' | '7654' | '7651' | '7652':
                return '3'
            case '7653':
                return '9'
            case '765394' | '765392' | '765391':
                return '8'
            case '765398':
                return '1'

            case '73':
                return '9'
            case '7396' | '7395' | '7394' | '7392' | '7391':
                return '8'
            case '7398':
                return '1'
            case '739816' | '739815' | '739812':
                return '4'
            case '739814':
                return '5'

            case '72':
                return '5'
            case '7258' | '7259' | '7256' | '7254' | '7251':
                return '3'
            case '7253':
                return '1'
            case '725318' | '725319' | '725316':
                return '4'
            case '725314':
                return '9'

            case '71':
                return '9'
            case '7194' | '7195' | '7196' | '7193' | '7192':
                return '8'
            case '7198':
                return '3'
            case '719834' | '719835' | '719832':
                return '6'
            case '719836':
                return '5'

            case '74':
                return '5'
            case '7458' | '7459' | '7456' | '7452' | '7451':
                return '3'
            case '7453':
                return '9'
            case '745396' | '745392' | '745391':
                return '8'
            case '745398':
                return '1'

            case '75':
                return '3'
            case '7538':
                return '2'
            case '75382':
                return ''
            case '753829' | '753826' | '753824':
                return '1'
            case '753821':
                return '9'
            case '75382194':
                return '6'
            case '75382196':
                return '4'

            case '7536':
                return '4'
            case '753648' | '753649' | '753642':
                return '1'
            case '753641':
                return '9'
            case '75364198':
                return '2'
            case '75364192':
                return '8'

            case '7532':
                return '8'
            case '753286' | '753284' | '753281':
                return '9'
            case '753289':
                return '1'
            case '75328916':
                return '4'
            case '75328914':
                return '6'

            case '7534':
                return '6'
            case '753468' | '753462' | '753461':
                return '9'
            case '753469':
                return '1'
            case '75346918':
                return '2'
            case '75346912':
                return '8'

            case '7539':
                return '1'
            case '753918' | '753916' | '753912':
                return '4'
            case '753914':
                return '2'

            case '7531':
                return '9'
            case '753198' | '753194' | '753192':
                return '6'
            case '753196':
                return '8'
            case '75239':
                return '8'
            case '7523984' | '7523986':
                return '1'
            case '7523981':
                return '4'

            case '15697':
                return '4'
            case '1569742' | '1569748':
                return '3'
            case '1569743':
                return '2'

            case '35871':
                return '2'
            case '3587126' | '3587124':
                return '9'
            case '3587129':
                return '6'

            case '95413':
                return '6'
            case '9541368' | '9541362':
                return '7'
            case '9541367':
                return '8'
