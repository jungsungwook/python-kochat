# MATRIX2B CHATBOT

## ENVIRONMENT & REQUIREMENTS
- python == 3.8.10 (64bit)
- pip == 23.0.1
- setuptools : 56.0.0
- Jinja2 == 3.0.3
- itsdangerous == 2.0.1
- werkzeug == 2.0.3
- pip3 install torch torchvision torchaudio
- tweepy == 3.10.0
- kocrawl == 1.0.9
- pip install JPype1-1.1.2-cp38-cp38-win_amd64.whl( file in local )
- JDK == openJDK 1.8.0_251 --> issue! 

## VENV GUIDE
create env : 

    py -[python-version] -m venv [folder-name]
    ex >  py -3.8 -m venv env

use project env(package) : 

    .\[folder-name]\Scripts\activate
    ex > .\env\Scripts\activate
    [!] 만약 보안오류 발생 시 관리자 권한으로 진행.
    [!] 그래도 안된다면 다음 명령어를 통해 권한 부여
    > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    [!] 최초 env 진입 시 pip 업그레이드 해주세요.

use local env(package) : 

    .\[folder-name]\Scripts\deactivate || deactivate
    ex > .\env\Scripts\deactivate || deactivate


## ISSUE
kochat 라이브러리는 2020년 이후 개발이 중단되어, 여러가지 이슈가 있어 해결법을 찾아 아래에 기록하고 있으니 참고하세요.
### 1)
> FutureWarning: Unlike other reduction functions (e.g. `skew`, `kurtosis`), the default behavior of `mode` typically preserves the axis it acts along. In SciPy 1.11.0, this behavior will change: the default value of `keepdims` will become False, the `axis` over which the statistic is taken will be eliminated, and the value None will no longer be accepted. Set `keepdims` to True or False to avoid this warning.

this Issue can solved. try it :
> \Lib\site-packages\sklearn\neighbors\_classification.py<br/><br/>
line 189 : mode, _ = stats.mode(_y[neigh_ind, k], axis=1)<br/>
=>  mode, _ = stats.mode(_y[neigh_ind, k], axis=1, keepdims=false)