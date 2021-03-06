<!--
Copyright 2017 F5 Networks Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Contributing Guide for networking-f5
If you have found this that means you you want to help us out. Thanks in advance for lending a hand! This guide should 
get you up and running quickly and make it easy for you to contribute. If we don't answer your questions here and you want to help or just say hi, hit us up on [Slack](https://f5-openstack-slack.herokuapp.com/).

## Issues
Creating issues is good; creating good issues is even better. Filing meaningful bug reports with lots of information  in them helps us figure out what to fix when and how it impacts our users. We like bugs because it means people are using our code, and we like fixing them even more.
 
## Pull Requests
If you are submitting a pull request you need to make sure that you have done a few things first:

* If a corresponding issue doesn't exist, file one.
* Make sure you have tested your code because we are going to do that when when you make your PR. You don't want 
_The Hat_ because your request fails unit tests.
* Clean up your git history because no one wants to see 75 commits for one issue.
* Use our [commit template](.git-commit-template.txt).
* Use our pull request template (below).

```
@<reviewer_id>
#### What issues does this address?
Fixes #<issueid>
WIP #<issueid>
...

#### What's this change do?

#### Where should the reviewer start?

#### Any background context?
```

## Testing
Creating tests is pretty straight forward and we need you to help us keep ensure
the quality of our code. We write both our unit tests and functional tests
using [pytest](http://pytest.org). We know it is extra work to write these
tests, but the maintainers and consumers of this code appreciate the effort and writing the tests is pretty easy.
 
Running those tests is even easier.
 
```
$ py.test --cov ./ --cov-report=html
$ open htmlcov/index.html
```

If you are running our functional tests you will need a real BIG-IP to run 
them against; you can get one of those pretty easily in [Amazon EC2](https://aws.amazon.com/marketplace/pp/B00JL3UASY/ref=srh_res_product_title?ie=UTF8&sr=0-10&qid=1449332167461).

## Documentation

This project uses CI/CD to build, test, and deploy documentation.

**Tools:**
- `sphinx`: builds HTML, checks syntax, and tests links.
- [f5-sphinx-theme](https://github.com/f5devcentral/f5-sphinx-theme): F5 theme for sphinx projects.
- `write-good`: tests grammar.
- Travis-CI: builds, tests, and deploys documentation.
- AWS S3: static website hosting.

**Scripts:**
- *deploy-docs*: Runs a Docker container with the credentials required to publish to clouddocs.f5.com.
- *docker-docs*: Runs a Docker container mounted to the current working directory.
- *test-docs*: runs the HTML build, grammar check, and linkcheck.

See the [Makefile](/Makefile) for more information.


### Build and Test Docs
You can use the commands below to build and test documentation changes.
Commands beginning with `docker` run in a Docker container using the same image used in Travis-CI ([f5devcentral/containthedocs](https://hub.docker.com/r/f5devcentral/containthedocs/)).

Note: If you don't use the Docker container, you need to install the project dependencies locally.

```
virtualenv <my-venv>
pip install -r requirements.txt
npm install write-good
```

| Command                | Description                                            |  
|------------------------|--------------------------------------------------------|
| `make html`            | basic HTML build                                       |
| `make preview`         | builds docs as you write; view changes live in browser |
| `make docs-test`       | run the docs tests                                     |  
| `make docker-docs`     | basic HTML build in a Docker container                 |
| `make docker-preview`  | builds docs in a Docker container as you write         |
| `make docker-test`     | runs docs tests in a Docker container                  |


## License
 
### Apache V2.0
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 
http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 
### Contributor License Agreement
Individuals or business entities who contribute to this project must have completed and submitted the [F5 Contributor License Agreement](http://clouddocs.f5.com/cloud/openstack/latest/support/cla_landing.html) to Openstack_CLA@f5.com prior to their code submission being included in this project.
