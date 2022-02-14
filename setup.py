from distutils.core import setup

setup(
    name='fastapi_response_log',  # How you named your package folder (MyLib)
    packages=['fastapi_response_log'],  # Chose the same as "name"
    version='0.1.0',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='A FastAPI route for logging every request',  # Give a short description about your library
    author='Albert',  # Type in your name
    author_email='',  # Type in your E-Mail
    url='https://github.com/aravindalbert/fastapi-log.git',  # Provide either the link to your github or to your website
    keywords=['fastaAPI', 'logging', 'response'],  # Keywords that define your package best
    install_requires=['starlette',
                      'user_agents',
                      'pydantic',
                      'fastapi',
                      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
