import os
import sys
import json
import subprocess

args = sys.argv

if len(args) < 1:
    print('Too few arguments passed extract_potentials.py')
    exit(1)

runs = args[1:]
print(f'runs: {runs}')

OS = 'UNIX-LIKE' if any([s in sys.platform for s in ['darwin', 'linux']]) else 'WINDOWS'

def load(config_path: str):
    with open(config_path, "r") as handle:
        return json.load(handle)

if OS == 'UNIX-LIKE':
    env_path = os.path.join('..', 'configs', 'env', 'unix.json')
elif OS == 'WINDOWS':
    env_path = os.path.join('..', 'configs', 'env', 'windows.json')

# load env.json
if os.path.exists(env_path):
    env: dict = load(env_path)

def handoff(env: dict, run_number: int):
    comsol_path = env['COMSOL_PATH']
    jdk_path = env['JDK_PATH']
    project_path = env['PROJECT_PATH']
    
    run_path = os.path.join(project_path, 'configs', 'runs', f'{run_number}.json')
    core_name = 'ModelWrapper'
    if sys.platform.startswith('darwin'):  # macOS
        subprocess.Popen(['{}/bin/comsol'.format(comsol_path), 'server'], close_fds=True)
        os.system(
            '{}/javac -classpath ../bin/json-20190722.jar:{}/plugins/* model/*.java -d ../bin'.format(jdk_path,
                                                                                                      comsol_path))
        # https://stackoverflow.com/questions/219585/including-all-the-jars-in-a-directory-within-the-java-classpath
        os.system('{}/java/maci64/jre/Contents/Home/bin/java '
                  '-cp .:$(echo {}/plugins/*.jar | '
                  'tr \' \' \':\'):../bin/json-20190722.jar:../bin model.{} "{}" "{}"'.format(comsol_path,
                                                                                              comsol_path,
                                                                                              core_name,
                                                                                              project_path,
                                                                                              run_path))
        # os.chdir('..')
    elif sys.platform.startswith('linux'):  # linux
        subprocess.Popen(['{}/bin/comsol'.format(comsol_path), 'server'], close_fds=True)
        os.system(
            '{}/javac -classpath ../bin/json-20190722.jar:{}/plugins/* model/*.java -d ../bin'.format(jdk_path,
                                                                                                      comsol_path))
        # https://stackoverflow.com/questions/219585/including-all-the-jars-in-a-directory-within-the-java-classpath
        os.system('{}/java/glnxa64/jre/bin/java '
                  '-cp .:$(echo {}/plugins/*.jar | '
                  'tr \' \' \':\'):../bin/json-20190722.jar:../bin model.{} "{}" "{}"'.format(comsol_path,
                                                                                              comsol_path,
                                                                                              core_name,
                                                                                              project_path,
                                                                                              run_path))
        # os.chdir('..')
    else:  # assume to be 'win64'
        subprocess.Popen(['{}\\bin\\win64\\comsolmphserver.exe'.format(comsol_path)], close_fds=True)
        os.system('""{}\\javac" '
                  '-cp "..\\bin\\json-20190722.jar";"{}\\plugins\\*" '
                  'model\\*.java -d ..\\bin"'.format(jdk_path,
                                                     comsol_path))
        os.system('""{}\\java\\win64\\jre\\bin\\java" '
                  '-cp "{}\\plugins\\*";"..\\bin\\json-20190722.jar";"..\\bin" '
                  'model.{} "{}" "{}""'.format(comsol_path,
                                               comsol_path,
                                               core_name,
                                               project_path,
                                               run_path))
        # os.chdir('..')

for run in runs:
    handoff(env, int(run))

print('=========== DONE ===========')
exit(1)
