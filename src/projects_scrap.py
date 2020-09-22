# body > section > div:nth-child(1) > article > div > ul:nth-child(16)

from bs4 import BeautifulSoup


def scrap_projects():
    repos = []
    with open('projects.html', 'r') as html:
        contents = html.read()
        soup = BeautifulSoup(contents, 'lxml')
        for tag in soup.find_all('code'):
            repos.append(tag.text)
    return repos


candidate_repos = ['32xlevel/iscanner', 'a5kin/xentica', 'altiore/altiore.ui', 'brucegithub/namespace-protector', 'btraceio/btrace', 'catalyst-team/catalyst', 'coderaiser/cloudcmd', 'covid19cz/erouska-android', 'crocinc/sql-boot', 'cybercog/laravel-love', 'decorators-squad/eo-yaml', 'dgroup/lazylead', 'dotenv-linter/dotenv-linter', 'embox/embox', 'fagnermartinsbrack/jack-the-moneylender', 'fleksl/avatar-maker', 'flyimg/flyimg', 'geftimov/android-pathview', 'gentee/gentee', 'gulpjs/gulp', 'hdouss/jeometry', 'iakunin/codexia-bot', 'ibitcy/eo-locale', 'igorwojda/android-showcase', 'imrafaelmerino/json-values', 'javascript-obfuscator/javascript-obfuscator', 'ligi/survivalmanual', 'mangstadt/print-from-phone', 'mayokunthefirst/instant-weather', 'mcjtymods/rftoolscontrol', 'msaaddev/github-interact-cli', 'muhammad-usama-aleem/glasses-to-aid-the-blind', 'munusphp/munus', 'nesbox/tic-80',  'onqtam/doctest', 'openfeign/feign', 'pholser/junit-quickcheck', 'pikvm/pikvm', 'pixelpusher/liveprinter', 'pmed/v8pp', 'popovevgeniy/swgf', 'pric/pric', 'r57zone/easynotes', 'reactos/reactos', 'reddec/trusted-cgi', 'reinterpretcat/vrp', 'rey5137/jsonbatch', 'rus4j/trigger-collections', 'scalikejdbc/scalikejdbc', 'scommons/scommons-react-native', 'sgjava/java-periphery', 'stagedml/stagedml', 'stiffstream/restinio', 'tolsi/dataragon', 'totumonline/totum-mit', 'traccar/traccar', 'tyvik/geopuzzle', 'victorx64/devrating', 'wentout/mnemonica', 'wildfish/crispy-forms-gds', 'yuriykulikov/alarmclock', 'z7zmey/php-parser']
print(f"Repos: {candidate_repos}")
