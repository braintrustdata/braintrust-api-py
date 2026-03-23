# Changelog

## 0.7.0 (2026-03-23)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.6.0...v0.7.0)

### Features

* **api:** manual updates ([#118](https://github.com/braintrustdata/braintrust-api-py/issues/118)) ([63e202c](https://github.com/braintrustdata/braintrust-api-py/commit/63e202cd387287b5c64ad13192936ea0bbcbb42f))
* **api:** manual updates ([#119](https://github.com/braintrustdata/braintrust-api-py/issues/119)) ([de6baa4](https://github.com/braintrustdata/braintrust-api-py/commit/de6baa43686443d4f8619accd954f6fbb9049829))
* **api:** manual updates ([#120](https://github.com/braintrustdata/braintrust-api-py/issues/120)) ([5ad9b62](https://github.com/braintrustdata/braintrust-api-py/commit/5ad9b62ea0b4dffb52072155f9b5294f9a4967b7))
* clean up environment call outs ([f89c278](https://github.com/braintrustdata/braintrust-api-py/commit/f89c2780a0064e43845db4030546b72187f0f2d2))
* **client:** add follow_redirects request option ([bc631ed](https://github.com/braintrustdata/braintrust-api-py/commit/bc631ed66ad6b580a40ab72ef7593abaf7130da7))
* **client:** add support for aiohttp ([4cb377e](https://github.com/braintrustdata/braintrust-api-py/commit/4cb377ebfe133785ac7db18b25d3a16cb476c2bd))
* **client:** allow passing `NotGiven` for body ([#109](https://github.com/braintrustdata/braintrust-api-py/issues/109)) ([6e07ab6](https://github.com/braintrustdata/braintrust-api-py/commit/6e07ab68da42fc2b244fecae9b787df4ee4d6644))
* **client:** send `X-Stainless-Read-Timeout` header ([#104](https://github.com/braintrustdata/braintrust-api-py/issues/104)) ([ad27414](https://github.com/braintrustdata/braintrust-api-py/commit/ad27414c3490577fb574a604e9c1f1b3bd09ba29))
* **client:** support file upload requests ([220e8ca](https://github.com/braintrustdata/braintrust-api-py/commit/220e8ca5c3a4bbde813cb8abfa16475986a48e56))
* improve future compat with pydantic v3 ([5da7ac1](https://github.com/braintrustdata/braintrust-api-py/commit/5da7ac1d4d33a6bd3563eaa55e7e713e0e112383))
* **types:** replace List[str] with SequenceNotStr in params ([ed5d3b9](https://github.com/braintrustdata/braintrust-api-py/commit/ed5d3b9bbf84518bdb1054a6c10731bdf07f0d05))


### Bug Fixes

* **api:** better support union schemas with common properties ([#92](https://github.com/braintrustdata/braintrust-api-py/issues/92)) ([eef2c15](https://github.com/braintrustdata/braintrust-api-py/commit/eef2c157acc0d1b806fcd9d70fb7f520e7f4571d))
* asyncify on non-asyncio runtimes ([#108](https://github.com/braintrustdata/braintrust-api-py/issues/108)) ([138ac15](https://github.com/braintrustdata/braintrust-api-py/commit/138ac1530b39534c731274ef16518665cf315092))
* avoid newer type syntax ([ce333f0](https://github.com/braintrustdata/braintrust-api-py/commit/ce333f09533b9705680c9bb7e278c96e73c5ab0d))
* **ci:** correct conditional ([93ac1d6](https://github.com/braintrustdata/braintrust-api-py/commit/93ac1d6e5c5b69b328be077432ae5293fdeea0e8))
* **ci:** ensure pip is always available ([#123](https://github.com/braintrustdata/braintrust-api-py/issues/123)) ([7641012](https://github.com/braintrustdata/braintrust-api-py/commit/76410123efa7c43abbcf29110f3d5d43641c16d3))
* **ci:** release-doctor — report correct token name ([e4c6c12](https://github.com/braintrustdata/braintrust-api-py/commit/e4c6c1284c02c5f362b8a13202717f5b36bba29f))
* **ci:** remove publishing patch ([#124](https://github.com/braintrustdata/braintrust-api-py/issues/124)) ([8460bae](https://github.com/braintrustdata/braintrust-api-py/commit/8460bae94cef5668480604dcd4c14d141319ec52))
* **client:** close streams without requiring full consumption ([368e476](https://github.com/braintrustdata/braintrust-api-py/commit/368e4761887febaa971676b1b0eeac5bdec93842))
* **client:** correctly parse binary response | stream ([3825cae](https://github.com/braintrustdata/braintrust-api-py/commit/3825cae89943c2e6dd749a8198c5023f3e4a89e3))
* **client:** don't send Content-Type header on GET requests ([61555e0](https://github.com/braintrustdata/braintrust-api-py/commit/61555e030e0442811e679e248d245409ed4b117d))
* **client:** mark some request bodies as optional ([6e07ab6](https://github.com/braintrustdata/braintrust-api-py/commit/6e07ab68da42fc2b244fecae9b787df4ee4d6644))
* **client:** only call .close() when needed ([#89](https://github.com/braintrustdata/braintrust-api-py/issues/89)) ([0d60c0e](https://github.com/braintrustdata/braintrust-api-py/commit/0d60c0e36a6eb08c673861abd84f155bf87c03a5))
* compat with Python 3.14 ([cb4d371](https://github.com/braintrustdata/braintrust-api-py/commit/cb4d371b84774d2f1eb237318857f3d2d998d24a))
* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([332d176](https://github.com/braintrustdata/braintrust-api-py/commit/332d1769976543d04dd9778687a6862efbffb27c))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([0d74069](https://github.com/braintrustdata/braintrust-api-py/commit/0d74069298fbda114018fc93ed24392a678daefa))
* correctly handle deserialising `cls` fields ([#94](https://github.com/braintrustdata/braintrust-api-py/issues/94)) ([e9a5800](https://github.com/braintrustdata/braintrust-api-py/commit/e9a580024e79ca38512df3a21469b4f5583efae2))
* **docs/api:** remove references to nonexistent types ([5b74eb6](https://github.com/braintrustdata/braintrust-api-py/commit/5b74eb62ba33bbdda1d3486613358c38a2ab7a1b))
* ensure streams are always closed ([6f0fd91](https://github.com/braintrustdata/braintrust-api-py/commit/6f0fd91f8c91be27073135bcb3bd9696d9e36853))
* **package:** support direct resource imports ([12d747b](https://github.com/braintrustdata/braintrust-api-py/commit/12d747b10dc9027ecde7a915f997af3ac984dbfb))
* **parsing:** correctly handle nested discriminated unions ([e68d6c9](https://github.com/braintrustdata/braintrust-api-py/commit/e68d6c9ccce0018d67bab9e5c41c2579115e569a))
* **parsing:** ignore empty metadata ([927d97a](https://github.com/braintrustdata/braintrust-api-py/commit/927d97a71d41e2d2ba27533e1fec05f06be70403))
* **parsing:** parse extra field types ([1cc2d17](https://github.com/braintrustdata/braintrust-api-py/commit/1cc2d177dcb50cebed591014c89becfcae3cf73c))
* **perf:** optimize some hot paths ([3dd3ca6](https://github.com/braintrustdata/braintrust-api-py/commit/3dd3ca676e4aad9c2220bf7857492aa68b925a75))
* **perf:** skip traversing types for NotGiven values ([827644c](https://github.com/braintrustdata/braintrust-api-py/commit/827644c0a85fa054948ef4b5d2edac61fa918ff1))
* **pydantic v1:** more robust ModelField.annotation check ([3bad66b](https://github.com/braintrustdata/braintrust-api-py/commit/3bad66bec3b13849836f9778fc7a489565a07053))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([d24e16f](https://github.com/braintrustdata/braintrust-api-py/commit/d24e16fdfa9813cdc69a3f215d41e710ab2ab2dd))
* **tests:** make test_get_platform less flaky ([#97](https://github.com/braintrustdata/braintrust-api-py/issues/97)) ([b18604c](https://github.com/braintrustdata/braintrust-api-py/commit/b18604c0c77ebae9899a0924f961353177143d08))
* **types:** add missing total=False ([#126](https://github.com/braintrustdata/braintrust-api-py/issues/126)) ([47d4c8b](https://github.com/braintrustdata/braintrust-api-py/commit/47d4c8b87d1b7fe5bd243d1e285448af6734d378))
* **types:** handle more discriminated union shapes ([#122](https://github.com/braintrustdata/braintrust-api-py/issues/122)) ([45bc1ee](https://github.com/braintrustdata/braintrust-api-py/commit/45bc1ee93ec0d2f9509bc2af7de789014625d042))


### Chores

* add missing isclass check ([#87](https://github.com/braintrustdata/braintrust-api-py/issues/87)) ([6147129](https://github.com/braintrustdata/braintrust-api-py/commit/6147129e84523b054fe1b5c12cae911bcf56aba5))
* add Python 3.14 classifier and testing ([1176297](https://github.com/braintrustdata/braintrust-api-py/commit/1176297859fc3f69099dc3fef604d26bdb1a9c62))
* broadly detect json family of content-type headers ([3befdb8](https://github.com/braintrustdata/braintrust-api-py/commit/3befdb84c7948fdf2e94b7454c03e0591bc14ad1))
* bump `httpx-aiohttp` version to 0.1.9 ([daac88b](https://github.com/braintrustdata/braintrust-api-py/commit/daac88b9e1bd907c0d0a6ab2ab7ec60610dbd1a9))
* **ci:** add timeout thresholds for CI jobs ([49e9552](https://github.com/braintrustdata/braintrust-api-py/commit/49e95529290d86c47dfbb62f450df6d70dbcbce2))
* **ci:** change upload type ([68f25d4](https://github.com/braintrustdata/braintrust-api-py/commit/68f25d4a3610b9b3af9cc968ae6f1752ab20adfa))
* **ci:** enable for pull requests ([fac0113](https://github.com/braintrustdata/braintrust-api-py/commit/fac011355a92837cda2cc32d5ba2b73c2c6dcc89))
* **ci:** fix installation instructions ([6efadec](https://github.com/braintrustdata/braintrust-api-py/commit/6efadecfd1e735392810818df3cefd9a6b7ea880))
* **ci:** only run for pushes and fork pull requests ([14d6eba](https://github.com/braintrustdata/braintrust-api-py/commit/14d6eba95defcc7e919da78c64210396c1c7c997))
* **ci:** only use depot for staging repos ([d2ef77a](https://github.com/braintrustdata/braintrust-api-py/commit/d2ef77a165eb23d39d2b2afe5233303afb5b7d6e))
* **ci:** upload sdks to package manager ([8d74835](https://github.com/braintrustdata/braintrust-api-py/commit/8d748357a386e16bb8b5f226e7540b43fe946429))
* **client:** minor internal fixes ([cee4cc8](https://github.com/braintrustdata/braintrust-api-py/commit/cee4cc8d6b4d8a8a48a48d490349510ba7443a51))
* **client:** simplify `Optional[object]` to just `object` ([#86](https://github.com/braintrustdata/braintrust-api-py/issues/86)) ([2caa323](https://github.com/braintrustdata/braintrust-api-py/commit/2caa32373c587a8711612738f15f7f71781e467f))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([c8fe9e4](https://github.com/braintrustdata/braintrust-api-py/commit/c8fe9e49287cab88790de610e724f0ea3a8bc7a9))
* do not install brew dependencies in ./scripts/bootstrap by default ([6bb6f8b](https://github.com/braintrustdata/braintrust-api-py/commit/6bb6f8b489bf3a9d38e1ffeda0a5f23becfe3aa1))
* **docs:** grammar improvements ([d1cb254](https://github.com/braintrustdata/braintrust-api-py/commit/d1cb254e7697d173a5c9ab90bc896751239f80bc))
* **docs:** remove reference to rye shell ([460c7f4](https://github.com/braintrustdata/braintrust-api-py/commit/460c7f4cba44eb302c902f754711a9817bdc38fc))
* **docs:** remove unnecessary param examples ([3b8e0c7](https://github.com/braintrustdata/braintrust-api-py/commit/3b8e0c75cfd730609afd84ec91571deab6172b38))
* **docs:** update client docstring ([#113](https://github.com/braintrustdata/braintrust-api-py/issues/113)) ([ff53598](https://github.com/braintrustdata/braintrust-api-py/commit/ff53598038787ddd581ec4f56e9f22cdee07175d))
* **docs:** use environment variables for authentication in code snippets ([eb1e80f](https://github.com/braintrustdata/braintrust-api-py/commit/eb1e80fa7e9619caf8830a426ae36cf23835de86))
* fix typos ([#125](https://github.com/braintrustdata/braintrust-api-py/issues/125)) ([be765a1](https://github.com/braintrustdata/braintrust-api-py/commit/be765a1078e62b593fab2d8fbc00fd3aa8acbfe0))
* **internal/tests:** avoid race condition with implicit client cleanup ([6fb44c4](https://github.com/braintrustdata/braintrust-api-py/commit/6fb44c45cc2d51ce7e80b26803313ede788dde83))
* **internal:** add Sequence related utils ([1cd4188](https://github.com/braintrustdata/braintrust-api-py/commit/1cd41887039d51406958f38f929a2a7dd7ca6596))
* **internal:** avoid errors for isinstance checks on proxies ([d000c3f](https://github.com/braintrustdata/braintrust-api-py/commit/d000c3f76b8c7ba4d58e35c2e754ab93a4989ae7))
* **internal:** avoid pytest-asyncio deprecation warning ([#98](https://github.com/braintrustdata/braintrust-api-py/issues/98)) ([1f5c64a](https://github.com/braintrustdata/braintrust-api-py/commit/1f5c64a32bec2f6622dce0ac4d67ec54fb6d8179))
* **internal:** base client updates ([df24cba](https://github.com/braintrustdata/braintrust-api-py/commit/df24cba57dc226160b4c76819078123f4fa34bb5))
* **internal:** bummp ruff dependency ([#103](https://github.com/braintrustdata/braintrust-api-py/issues/103)) ([7e27bb2](https://github.com/braintrustdata/braintrust-api-py/commit/7e27bb2517e15e582e9d47a3bb07d26131c1b0be))
* **internal:** bump httpx dependency ([#88](https://github.com/braintrustdata/braintrust-api-py/issues/88)) ([2e6af33](https://github.com/braintrustdata/braintrust-api-py/commit/2e6af33c45f5cc4c3dbaafa9a8eb5d96af2f5b25))
* **internal:** bump pinned h11 dep ([34e6151](https://github.com/braintrustdata/braintrust-api-py/commit/34e61516915770cde83a1e5564bb5ac54df0b391))
* **internal:** bump pydantic dependency ([#75](https://github.com/braintrustdata/braintrust-api-py/issues/75)) ([da0cbfa](https://github.com/braintrustdata/braintrust-api-py/commit/da0cbfa37f812145ea55fb0a73623375b0da08e7))
* **internal:** bump pyright version ([49b6a7a](https://github.com/braintrustdata/braintrust-api-py/commit/49b6a7a73717824276edd013542eecebcba16a3a))
* **internal:** bump rye to 0.44.0 ([#121](https://github.com/braintrustdata/braintrust-api-py/issues/121)) ([e56560b](https://github.com/braintrustdata/braintrust-api-py/commit/e56560b58bbeda8956f50c650316ee68cb9ccfc4))
* **internal:** change ci workflow machines ([0e8211a](https://github.com/braintrustdata/braintrust-api-py/commit/0e8211a0361f807306a982057615f0312ef1558a))
* **internal:** change default timeout to an int ([#102](https://github.com/braintrustdata/braintrust-api-py/issues/102)) ([aa430f5](https://github.com/braintrustdata/braintrust-api-py/commit/aa430f5fe78304735e3bfb9f436bfec743051db5))
* **internal:** codegen related update ([2c6433b](https://github.com/braintrustdata/braintrust-api-py/commit/2c6433be80ba63901d59523886cdbcef627fafed))
* **internal:** codegen related update ([7b6e6d6](https://github.com/braintrustdata/braintrust-api-py/commit/7b6e6d61d715d4d802c5e0aa7968a69a74d27b5a))
* **internal:** codegen related update ([#101](https://github.com/braintrustdata/braintrust-api-py/issues/101)) ([2083784](https://github.com/braintrustdata/braintrust-api-py/commit/208378450079cd399c9dbaa42dd847ee4e3d8d7b))
* **internal:** codegen related update ([#72](https://github.com/braintrustdata/braintrust-api-py/issues/72)) ([5e4b37b](https://github.com/braintrustdata/braintrust-api-py/commit/5e4b37b0c9818359fbf4fb2016a614dd45cbdf9f))
* **internal:** codegen related update ([#77](https://github.com/braintrustdata/braintrust-api-py/issues/77)) ([fa673fd](https://github.com/braintrustdata/braintrust-api-py/commit/fa673fdf7805b5ae63b2a0b22aafffed93fa21c8))
* **internal:** codegen related update ([#78](https://github.com/braintrustdata/braintrust-api-py/issues/78)) ([934bb92](https://github.com/braintrustdata/braintrust-api-py/commit/934bb92fe83ac052499dbdc1aa3dbe6ebf607b85))
* **internal:** codegen related update ([#79](https://github.com/braintrustdata/braintrust-api-py/issues/79)) ([836fc31](https://github.com/braintrustdata/braintrust-api-py/commit/836fc3149e373106c45f926877be4fc5658f2399))
* **internal:** codegen related update ([#81](https://github.com/braintrustdata/braintrust-api-py/issues/81)) ([d4eca1c](https://github.com/braintrustdata/braintrust-api-py/commit/d4eca1c387ca337c78e815432362e6e3f4872b3d))
* **internal:** codegen related update ([#82](https://github.com/braintrustdata/braintrust-api-py/issues/82)) ([68ab6b3](https://github.com/braintrustdata/braintrust-api-py/commit/68ab6b3800c7cc03a12aa75e7ece33c609ca77d6))
* **internal:** codegen related update ([#85](https://github.com/braintrustdata/braintrust-api-py/issues/85)) ([b5193a7](https://github.com/braintrustdata/braintrust-api-py/commit/b5193a7ef2b555bbba8ba670336bb687633770d1))
* **internal:** codegen related update ([#91](https://github.com/braintrustdata/braintrust-api-py/issues/91)) ([e17d9fa](https://github.com/braintrustdata/braintrust-api-py/commit/e17d9fa0d1aab9d9f52a814a24c60e4fce31f324))
* **internal:** codegen related update ([#95](https://github.com/braintrustdata/braintrust-api-py/issues/95)) ([eeed899](https://github.com/braintrustdata/braintrust-api-py/commit/eeed899d4f5f30f9d5fc2263f2dcff5307661428))
* **internal:** detect missing future annotations with ruff ([c8690f3](https://github.com/braintrustdata/braintrust-api-py/commit/c8690f34fcb239cb55e4db90bc7fb4d572d64311))
* **internal:** expand CI branch coverage ([1fbeff3](https://github.com/braintrustdata/braintrust-api-py/commit/1fbeff3ac01f1cfadb7f4f715ac2a4ae4d1c306b))
* **internal:** fix devcontainers setup ([#110](https://github.com/braintrustdata/braintrust-api-py/issues/110)) ([1942380](https://github.com/braintrustdata/braintrust-api-py/commit/1942380bbd8a034e589bfbbdbfce7d807d0a38f9))
* **internal:** fix list file params ([40348db](https://github.com/braintrustdata/braintrust-api-py/commit/40348db2c3a33e90e7d25aab924208c057abcb52))
* **internal:** fix ruff target version ([dfaf940](https://github.com/braintrustdata/braintrust-api-py/commit/dfaf9401c48d575c6799ba78f9841f8365f24d53))
* **internal:** fix some typos ([#84](https://github.com/braintrustdata/braintrust-api-py/issues/84)) ([d8fe216](https://github.com/braintrustdata/braintrust-api-py/commit/d8fe216ef2a919de855c0de211645401287649de))
* **internal:** fix type traversing dictionary params ([#105](https://github.com/braintrustdata/braintrust-api-py/issues/105)) ([39541c9](https://github.com/braintrustdata/braintrust-api-py/commit/39541c9f3d39fc37023c302fbec9d97cafc18ab0))
* **internal:** grammar fix (it's -&gt; its) ([fc9d94f](https://github.com/braintrustdata/braintrust-api-py/commit/fc9d94f9171b82fcd60685072660c11d590acb82))
* **internal:** import reformatting ([5a7a874](https://github.com/braintrustdata/braintrust-api-py/commit/5a7a8745f19eb550b311bc439f2c6d7e5ed080e3))
* **internal:** minor formatting changes ([13a53a3](https://github.com/braintrustdata/braintrust-api-py/commit/13a53a3c11a6c1ba1f3c1460c62220fdefd9f618))
* **internal:** minor formatting changes ([#100](https://github.com/braintrustdata/braintrust-api-py/issues/100)) ([ef56b7d](https://github.com/braintrustdata/braintrust-api-py/commit/ef56b7deec376eb3696d18d5c2ea163fa7b350df))
* **internal:** minor style changes ([#99](https://github.com/braintrustdata/braintrust-api-py/issues/99)) ([ef7980e](https://github.com/braintrustdata/braintrust-api-py/commit/ef7980e70bc61777c8b4b2d57fe60600b32969df))
* **internal:** minor type handling changes ([#106](https://github.com/braintrustdata/braintrust-api-py/issues/106)) ([d4339f7](https://github.com/braintrustdata/braintrust-api-py/commit/d4339f732394a06262483ae645b311347b181b2d))
* **internal:** move mypy configurations to `pyproject.toml` file ([41d1fd4](https://github.com/braintrustdata/braintrust-api-py/commit/41d1fd446482235fbb5b3ca8eeb699e3a47bca0f))
* **internal:** properly set __pydantic_private__ ([#111](https://github.com/braintrustdata/braintrust-api-py/issues/111)) ([fdf56ff](https://github.com/braintrustdata/braintrust-api-py/commit/fdf56ffdbbd06c4b95114a79d05abeef7e9dfe79))
* **internal:** reduce CI branch coverage ([7fd60ea](https://github.com/braintrustdata/braintrust-api-py/commit/7fd60ea17aed75073fd1ea0397f0d5b40fef63cb))
* **internal:** refactor retries to not use recursion ([ae05f8f](https://github.com/braintrustdata/braintrust-api-py/commit/ae05f8f42898e175bfb945e50fe189a9878a2e16))
* **internal:** remove extra empty newlines ([#117](https://github.com/braintrustdata/braintrust-api-py/issues/117)) ([34df2f6](https://github.com/braintrustdata/braintrust-api-py/commit/34df2f6ab8bfcf51690c758bd7687b5ce873e043))
* **internal:** remove trailing character ([#127](https://github.com/braintrustdata/braintrust-api-py/issues/127)) ([bf384bd](https://github.com/braintrustdata/braintrust-api-py/commit/bf384bd4ef7fd27cc0bb707527e2d8a579e06fcc))
* **internal:** remove unused http client options forwarding ([#114](https://github.com/braintrustdata/braintrust-api-py/issues/114)) ([12a3eee](https://github.com/braintrustdata/braintrust-api-py/commit/12a3eee37d7e36babed7badec877acda236de437))
* **internal:** slight transform perf improvement ([#128](https://github.com/braintrustdata/braintrust-api-py/issues/128)) ([553e3ce](https://github.com/braintrustdata/braintrust-api-py/commit/553e3ce0ebafba74ff45c65383d090e2483a31f2))
* **internal:** update client tests ([#107](https://github.com/braintrustdata/braintrust-api-py/issues/107)) ([f43e7eb](https://github.com/braintrustdata/braintrust-api-py/commit/f43e7eb3913cc74799f208ba2578ac8e94f0fb4a))
* **internal:** update comment in script ([8ba181d](https://github.com/braintrustdata/braintrust-api-py/commit/8ba181d4baa521b5ddbb7e5de6e13bf1e74f5a5a))
* **internal:** update conftest.py ([ae3364b](https://github.com/braintrustdata/braintrust-api-py/commit/ae3364b374c3a1b1e6e18afe9cee08f13a2029ba))
* **internal:** update models test ([316af6f](https://github.com/braintrustdata/braintrust-api-py/commit/316af6fa7c1fc429bc10ec2b413d9c96084d0079))
* **internal:** update pydantic dependency ([5ce685b](https://github.com/braintrustdata/braintrust-api-py/commit/5ce685b87aa8b269c706fbe41124da6ac65c1d9a))
* **internal:** update pyright exclude list ([71fd220](https://github.com/braintrustdata/braintrust-api-py/commit/71fd22023a5153a3d7b0cd21ab8487921a6bd976))
* **internal:** update pyright settings ([f753908](https://github.com/braintrustdata/braintrust-api-py/commit/f75390899e84a57a4f9458492affac01a589b66b))
* **internal:** updated imports ([#80](https://github.com/braintrustdata/braintrust-api-py/issues/80)) ([95fbd1f](https://github.com/braintrustdata/braintrust-api-py/commit/95fbd1f1da95a51c319a873d2260fc8492010b65))
* make the `Omit` type public ([#74](https://github.com/braintrustdata/braintrust-api-py/issues/74)) ([76dbaf6](https://github.com/braintrustdata/braintrust-api-py/commit/76dbaf64dfed92a14d3d1825107ecad2a49a49b5))
* **package:** drop Python 3.8 support ([37d9089](https://github.com/braintrustdata/braintrust-api-py/commit/37d90893dcab350d67c4c65aca5ac1df79e0e6fc))
* **package:** mark python 3.13 as supported ([08e67ff](https://github.com/braintrustdata/braintrust-api-py/commit/08e67ff0b307707a5832c836d4d48d6fc3eb1e82))
* Pin github actions to commit ([#130](https://github.com/braintrustdata/braintrust-api-py/issues/130)) ([88a9527](https://github.com/braintrustdata/braintrust-api-py/commit/88a95273acabe9c1baa797438899e4ce48544e07))
* **project:** add settings file for vscode ([22b6ad6](https://github.com/braintrustdata/braintrust-api-py/commit/22b6ad61b6bcbc411ed03dc836a72028fab8f6fb))
* **readme:** fix version rendering on pypi ([e3b94a9](https://github.com/braintrustdata/braintrust-api-py/commit/e3b94a9b15f6a121726bbb390bc5aec433e94d9c))
* **readme:** update badges ([d8a93b0](https://github.com/braintrustdata/braintrust-api-py/commit/d8a93b0ee8468f4261c411e8a69489e0f5e2beb8))
* **tests:** add tests for httpx client instantiation & proxies ([88ee490](https://github.com/braintrustdata/braintrust-api-py/commit/88ee490f8a04de38f3b39c2d3d3016aca77b6191))
* **tests:** run tests in parallel ([d99e688](https://github.com/braintrustdata/braintrust-api-py/commit/d99e6889101cfcecd3b0fb5c55f0fc522e44d85f))
* **tests:** simplify `get_platform` test ([f84e074](https://github.com/braintrustdata/braintrust-api-py/commit/f84e07449429fc1056aa2daaf4a49fdd0c9fcca9))
* **tests:** skip some failing tests on the latest python versions ([3d9df0b](https://github.com/braintrustdata/braintrust-api-py/commit/3d9df0ba3d0852c159e43ddfc5097b71a555529c))
* **types:** change optional parameter type from NotGiven to Omit ([87710bf](https://github.com/braintrustdata/braintrust-api-py/commit/87710bfbeb63bd9221163d3ec26befe24768ed99))
* update @stainless-api/prism-cli to v5.15.0 ([7da60e9](https://github.com/braintrustdata/braintrust-api-py/commit/7da60e9af1f23566618da1a3c7ae008449e8c054))
* update github action ([a03992a](https://github.com/braintrustdata/braintrust-api-py/commit/a03992ac7fe6ebdee6a28a8639828aabe4189058))
* update lockfile ([0dd4858](https://github.com/braintrustdata/braintrust-api-py/commit/0dd485835b435bf3bc605062545bdec54ccb8665))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([98234df](https://github.com/braintrustdata/braintrust-api-py/commit/98234dfdcdefed8d3f21705c7d13baa7f6d3f5d6))
* fix typos ([#90](https://github.com/braintrustdata/braintrust-api-py/issues/90)) ([d75a8d5](https://github.com/braintrustdata/braintrust-api-py/commit/d75a8d54a94798a565352454b000b90fce6e08bd))
* **raw responses:** fix duplicate `the` ([#96](https://github.com/braintrustdata/braintrust-api-py/issues/96)) ([d13b829](https://github.com/braintrustdata/braintrust-api-py/commit/d13b829fd7267d2a3fd5fdea9003f04d45910af0))
* **readme:** example snippet for client context manager ([#83](https://github.com/braintrustdata/braintrust-api-py/issues/83)) ([471d048](https://github.com/braintrustdata/braintrust-api-py/commit/471d048b5e5d48d5045aee2e4c1aa345e5ecca98))
* **readme:** fix http client proxies example ([#76](https://github.com/braintrustdata/braintrust-api-py/issues/76)) ([16a3429](https://github.com/braintrustdata/braintrust-api-py/commit/16a342939bd4a73e9d46ba3789f1c2bec480e725))
* revise readme docs about nested params ([#115](https://github.com/braintrustdata/braintrust-api-py/issues/115)) ([f3cc5cd](https://github.com/braintrustdata/braintrust-api-py/commit/f3cc5cd5952845923a98411ca5ebac8eccd2b581))
* update URLs from stainlessapi.com to stainless.com ([#112](https://github.com/braintrustdata/braintrust-api-py/issues/112)) ([c9d003a](https://github.com/braintrustdata/braintrust-api-py/commit/c9d003a7b026675792ca0f23af1dbc1a89997f2e))

## 0.6.0 (2024-11-28)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([#45](https://github.com/braintrustdata/braintrust-api-py/issues/45)) ([5240c3b](https://github.com/braintrustdata/braintrust-api-py/commit/5240c3b1ac7c21c88d7ec901aedcb2e2020688d0))
* **api:** manual updates ([#56](https://github.com/braintrustdata/braintrust-api-py/issues/56)) ([5d8fc1c](https://github.com/braintrustdata/braintrust-api-py/commit/5d8fc1cfc7d8e855aa190baba405d967948e7701))
* **api:** manual updates ([#57](https://github.com/braintrustdata/braintrust-api-py/issues/57)) ([02d31da](https://github.com/braintrustdata/braintrust-api-py/commit/02d31da07fac7f5ab98db7606aafcaf9aa29a410))
* **api:** manual updates ([#59](https://github.com/braintrustdata/braintrust-api-py/issues/59)) ([d1189cb](https://github.com/braintrustdata/braintrust-api-py/commit/d1189cb307b7c5539a74fbf13bb3719f700ea559))
* **api:** manual updates ([#60](https://github.com/braintrustdata/braintrust-api-py/issues/60)) ([f23c2b7](https://github.com/braintrustdata/braintrust-api-py/commit/f23c2b726a01ce717d5ce5bf5408f3b29cf3e125))
* **api:** manual updates ([#61](https://github.com/braintrustdata/braintrust-api-py/issues/61)) ([561a9df](https://github.com/braintrustdata/braintrust-api-py/commit/561a9df7c16c7e24e843aed8a2b38d6b69c0f0f3))
* **api:** manual updates ([#63](https://github.com/braintrustdata/braintrust-api-py/issues/63)) ([2b8194b](https://github.com/braintrustdata/braintrust-api-py/commit/2b8194bfd2836abe0c3cb972572d008dea0170a5))
* **api:** manual updates ([#64](https://github.com/braintrustdata/braintrust-api-py/issues/64)) ([9adb6de](https://github.com/braintrustdata/braintrust-api-py/commit/9adb6de5e711ee4892da6a9afcd236285fe3f725))
* **api:** manual updates ([#65](https://github.com/braintrustdata/braintrust-api-py/issues/65)) ([668565b](https://github.com/braintrustdata/braintrust-api-py/commit/668565ba2a73deac607fedcab42ce728ed2d6207))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#70](https://github.com/braintrustdata/braintrust-api-py/issues/70)) ([fecb2c9](https://github.com/braintrustdata/braintrust-api-py/commit/fecb2c9d2654b2e51c1979e8a70b361486f627d8))


### Chores

* **api:** manual updates ([#48](https://github.com/braintrustdata/braintrust-api-py/issues/48)) ([788fa24](https://github.com/braintrustdata/braintrust-api-py/commit/788fa24385808ca6adb1fb2ab944956d6c196bfa))
* **internal:** exclude mypy from running on tests ([#69](https://github.com/braintrustdata/braintrust-api-py/issues/69)) ([e017f4d](https://github.com/braintrustdata/braintrust-api-py/commit/e017f4d06e0d529e7c8ead11826f9a09124c4358))
* **internal:** fix compat model_dump method when warnings are passed ([#66](https://github.com/braintrustdata/braintrust-api-py/issues/66)) ([015cbf0](https://github.com/braintrustdata/braintrust-api-py/commit/015cbf08d0ed80ccf2a45d320f9618bdf0df268b))
* rebuild project due to codegen change ([#47](https://github.com/braintrustdata/braintrust-api-py/issues/47)) ([9383958](https://github.com/braintrustdata/braintrust-api-py/commit/93839586abae5c0800a41ec07097739990fb5b59))
* rebuild project due to codegen change ([#49](https://github.com/braintrustdata/braintrust-api-py/issues/49)) ([2a49159](https://github.com/braintrustdata/braintrust-api-py/commit/2a491598dcac8448483f55b0594a4c230e109b2d))
* rebuild project due to codegen change ([#50](https://github.com/braintrustdata/braintrust-api-py/issues/50)) ([43596d5](https://github.com/braintrustdata/braintrust-api-py/commit/43596d558404219f7b6e24668e88c66ac4a290d6))
* rebuild project due to codegen change ([#51](https://github.com/braintrustdata/braintrust-api-py/issues/51)) ([b4809a9](https://github.com/braintrustdata/braintrust-api-py/commit/b4809a910f59d9b122339c07a153dd4f1fe474eb))
* rebuild project due to codegen change ([#52](https://github.com/braintrustdata/braintrust-api-py/issues/52)) ([f07d013](https://github.com/braintrustdata/braintrust-api-py/commit/f07d0135a7a728510d49466d7bc76a6e37cc09f2))
* rebuild project due to codegen change ([#53](https://github.com/braintrustdata/braintrust-api-py/issues/53)) ([cbbaac1](https://github.com/braintrustdata/braintrust-api-py/commit/cbbaac15d47ad5b73a0e7dc9271a8905eaf28331))
* rebuild project due to codegen change ([#54](https://github.com/braintrustdata/braintrust-api-py/issues/54)) ([a0b0eeb](https://github.com/braintrustdata/braintrust-api-py/commit/a0b0eebfb8212ad52e246d1c90f16bb60fdb7d48))
* rebuild project due to codegen change ([#55](https://github.com/braintrustdata/braintrust-api-py/issues/55)) ([2a6e9c7](https://github.com/braintrustdata/braintrust-api-py/commit/2a6e9c7122066d9135d4bcef9eee851860e74e6a))
* rebuild project due to codegen change ([#58](https://github.com/braintrustdata/braintrust-api-py/issues/58)) ([0aa1951](https://github.com/braintrustdata/braintrust-api-py/commit/0aa1951835671f76c35a5a614b326d6b60b121f0))
* rebuild project due to codegen change ([#62](https://github.com/braintrustdata/braintrust-api-py/issues/62)) ([d67709a](https://github.com/braintrustdata/braintrust-api-py/commit/d67709a152147409b0f924372c75bf6e66719f65))
* remove now unused `cached-property` dep ([#68](https://github.com/braintrustdata/braintrust-api-py/issues/68)) ([dfc0a35](https://github.com/braintrustdata/braintrust-api-py/commit/dfc0a353e633bd7b816b0b174bc95b07c31d6ac8))


### Documentation

* add info log level to readme ([#67](https://github.com/braintrustdata/braintrust-api-py/issues/67)) ([ee4b200](https://github.com/braintrustdata/braintrust-api-py/commit/ee4b2003a38af4189adbaeb6263379f72417021a))

## 0.5.0 (2024-10-01)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.4.0...v0.5.0)

### Features

* **api:** deduplication ([#40](https://github.com/braintrustdata/braintrust-api-py/issues/40)) ([cfb6df3](https://github.com/braintrustdata/braintrust-api-py/commit/cfb6df32f085499136ba3774044e9b19767b0494))
* **api:** manual updates ([#41](https://github.com/braintrustdata/braintrust-api-py/issues/41)) ([024919b](https://github.com/braintrustdata/braintrust-api-py/commit/024919b2bd3e4d8d62cd6cdd268ea0e30e80ebe3))
* **api:** manual updates ([#42](https://github.com/braintrustdata/braintrust-api-py/issues/42)) ([d9a79c3](https://github.com/braintrustdata/braintrust-api-py/commit/d9a79c3cb6c10266ecdb28a3c662ded703143b25))
* **api:** manual updates ([#43](https://github.com/braintrustdata/braintrust-api-py/issues/43)) ([7220cd8](https://github.com/braintrustdata/braintrust-api-py/commit/7220cd8673b8391380410608acf381c39169c543))
* **api:** update via SDK Studio ([#25](https://github.com/braintrustdata/braintrust-api-py/issues/25)) ([769692c](https://github.com/braintrustdata/braintrust-api-py/commit/769692cb6eaf64bd0ccdb7542a1782bf77f4fca3))
* **api:** update via SDK Studio ([#30](https://github.com/braintrustdata/braintrust-api-py/issues/30)) ([0eaa454](https://github.com/braintrustdata/braintrust-api-py/commit/0eaa4541bdcaf64e0c5eb4e2b6940561da151d5e))
* **api:** update via SDK Studio ([#32](https://github.com/braintrustdata/braintrust-api-py/issues/32)) ([bac36b3](https://github.com/braintrustdata/braintrust-api-py/commit/bac36b3f1873b8915175798b21f475f0c91ce604))
* **api:** update via SDK Studio ([#33](https://github.com/braintrustdata/braintrust-api-py/issues/33)) ([dbb8d87](https://github.com/braintrustdata/braintrust-api-py/commit/dbb8d87d7e73757e82e6833d81932bb33a9e6e08))
* **api:** update via SDK Studio ([#34](https://github.com/braintrustdata/braintrust-api-py/issues/34)) ([dc8a983](https://github.com/braintrustdata/braintrust-api-py/commit/dc8a983807041c6da27175d9c5a158922d7d0e53))
* **api:** update via SDK Studio ([#35](https://github.com/braintrustdata/braintrust-api-py/issues/35)) ([2706ee9](https://github.com/braintrustdata/braintrust-api-py/commit/2706ee90a84d6577f63996502791095244a85ec6))
* **api:** update via SDK Studio ([#36](https://github.com/braintrustdata/braintrust-api-py/issues/36)) ([5bcdf52](https://github.com/braintrustdata/braintrust-api-py/commit/5bcdf522dca40ec9558160dbf1f9e0966cb7669e))
* **api:** update via SDK Studio ([#37](https://github.com/braintrustdata/braintrust-api-py/issues/37)) ([7b9b827](https://github.com/braintrustdata/braintrust-api-py/commit/7b9b827633a145eb5f396b0a243ac850864c7526))
* **client:** send retry count header ([#29](https://github.com/braintrustdata/braintrust-api-py/issues/29)) ([bffa1a1](https://github.com/braintrustdata/braintrust-api-py/commit/bffa1a121cf8c1fcfaf5ceb5273c98dc95a4c1f6))


### Bug Fixes

* **api:** fix go build ([#39](https://github.com/braintrustdata/braintrust-api-py/issues/39)) ([d72ac01](https://github.com/braintrustdata/braintrust-api-py/commit/d72ac01dd5a9dce5f84d304c1816765d8bace953))
* **api:** fix import bug ([8ea7257](https://github.com/braintrustdata/braintrust-api-py/commit/8ea7257a6d7cd40669a47665b784b3276dfbc479))
* **client:** handle domains with underscores ([#28](https://github.com/braintrustdata/braintrust-api-py/issues/28)) ([227a7b0](https://github.com/braintrustdata/braintrust-api-py/commit/227a7b0e14492670970c83636ad13f03b3f68fbe))


### Chores

* **internal:** codegen related update ([#26](https://github.com/braintrustdata/braintrust-api-py/issues/26)) ([6501ee7](https://github.com/braintrustdata/braintrust-api-py/commit/6501ee74269a56dacb3b0ba33068c3b43a0341d0))
* **internal:** codegen related update ([#38](https://github.com/braintrustdata/braintrust-api-py/issues/38)) ([e612fe4](https://github.com/braintrustdata/braintrust-api-py/commit/e612fe42607c0020803fd22f7776ba981a87d4d6))
* **internal:** update pydantic v1 compat helpers ([#31](https://github.com/braintrustdata/braintrust-api-py/issues/31)) ([b1af15f](https://github.com/braintrustdata/braintrust-api-py/commit/b1af15faa99d0a19c1af8343b99c94175cfa1ab9))

## 0.4.0 (2024-08-09)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.3.0...v0.4.0)

### Features

* **api:** update via SDK Studio ([87bbfe8](https://github.com/braintrustdata/braintrust-api-py/commit/87bbfe87803963c6475c8bc24512d82a547e0ff0))


### Chores

* go live ([#22](https://github.com/braintrustdata/braintrust-api-py/issues/22)) ([99bd9d5](https://github.com/braintrustdata/braintrust-api-py/commit/99bd9d5d6dc6adbc48ab211f7931259ead31d0e8))
* **internal:** ensure package is importable in lint cmd ([#23](https://github.com/braintrustdata/braintrust-api-py/issues/23)) ([fd7b4e1](https://github.com/braintrustdata/braintrust-api-py/commit/fd7b4e1377a78909075443388a64f4523db979e4))

## 0.3.0 (2024-08-09)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.2.0...v0.3.0)

### Features

* add model ProjectScoreCategory ([a8ddd18](https://github.com/braintrustdata/braintrust-api-py/commit/a8ddd18431e1d3a8748eb6820fa187f81c82fba9))
* **api:** manual updates ([076b4a3](https://github.com/braintrustdata/braintrust-api-py/commit/076b4a3ad138748fe2381ef2bafd66dd7c2e7b73))
* **api:** manual updates ([8e55dde](https://github.com/braintrustdata/braintrust-api-py/commit/8e55dde4fe05cbe49c1d6ec7eabd27ece7ec9671))
* **api:** manual updates ([#18](https://github.com/braintrustdata/braintrust-api-py/issues/18)) ([13677d2](https://github.com/braintrustdata/braintrust-api-py/commit/13677d242f620550baf6fe84d6f21dd8af0018d7))
* **api:** update via SDK Studio ([eb42e62](https://github.com/braintrustdata/braintrust-api-py/commit/eb42e62d44a3ea5db5a573972815e261ffa88edc))
* **api:** update via SDK Studio ([eea4b43](https://github.com/braintrustdata/braintrust-api-py/commit/eea4b432933accf85e6fcfb40f971a33a84019e7))
* **api:** update via SDK Studio ([ab63fec](https://github.com/braintrustdata/braintrust-api-py/commit/ab63fec431b330f786cc4a5f7464075c5b6c90af))
* **api:** update via SDK Studio ([9d9a2db](https://github.com/braintrustdata/braintrust-api-py/commit/9d9a2db5be33fc09f6d1a2dbffd3d966cab57749))
* **api:** update via SDK Studio ([9f56d25](https://github.com/braintrustdata/braintrust-api-py/commit/9f56d254037853cb05825d1007c48b50637d7b3e))
* **api:** update via SDK Studio ([3ec6506](https://github.com/braintrustdata/braintrust-api-py/commit/3ec6506e382a040e7cbefd2510523b5ba3cc541d))
* **api:** update via SDK Studio ([65e3db9](https://github.com/braintrustdata/braintrust-api-py/commit/65e3db9c9a4357fa8c7b3248c8bec057c9748168))
* **api:** update via SDK Studio ([7e2a816](https://github.com/braintrustdata/braintrust-api-py/commit/7e2a81671fccceaf44fd2b9d61f9d1245cf9d432))
* **api:** update via SDK Studio ([330baff](https://github.com/braintrustdata/braintrust-api-py/commit/330baff4f40f77d45b8552eade6be8c340639535))
* **api:** update via SDK Studio ([1d0b089](https://github.com/braintrustdata/braintrust-api-py/commit/1d0b0896570047542254809db0aec3b5dbc7e6cb))
* **api:** update via SDK Studio ([f32858c](https://github.com/braintrustdata/braintrust-api-py/commit/f32858cd4711888e4366a1b0bbe4db08ed4f4e25))
* **api:** update via SDK Studio ([c33f5d9](https://github.com/braintrustdata/braintrust-api-py/commit/c33f5d99474311ed0cd6b12f3abd3429d1a61eb5))
* **api:** update via SDK Studio ([4248329](https://github.com/braintrustdata/braintrust-api-py/commit/4248329824ea7a71a1d77ae4e1939542e1826685))
* **api:** update via SDK Studio ([7247c14](https://github.com/braintrustdata/braintrust-api-py/commit/7247c14cf9451ce8d881cba66e44e637bcbac524))
* **api:** update via SDK Studio ([faaec09](https://github.com/braintrustdata/braintrust-api-py/commit/faaec096ee7d529375b4a43f6ebd952cb6c53d98))
* **api:** update via SDK Studio ([76b05ec](https://github.com/braintrustdata/braintrust-api-py/commit/76b05ec43710202cd4f53c47d531a9339faffa6e))
* **api:** update via SDK Studio ([cc0a581](https://github.com/braintrustdata/braintrust-api-py/commit/cc0a581410ed9ec1f0e7fbe057dc7f49ab1adc3c))
* **api:** update via SDK Studio ([#10](https://github.com/braintrustdata/braintrust-api-py/issues/10)) ([99953df](https://github.com/braintrustdata/braintrust-api-py/commit/99953df954e08e897505149853c419576fb87f5e))
* **api:** update via SDK Studio ([#16](https://github.com/braintrustdata/braintrust-api-py/issues/16)) ([2a6ff71](https://github.com/braintrustdata/braintrust-api-py/commit/2a6ff7147783f0f54c6beb1cd51d209be1077776))


### Chores

* **ci:** bump prism mock server version ([77ae948](https://github.com/braintrustdata/braintrust-api-py/commit/77ae948770c73753f51ae84b9ea6691792dd2123))
* fix error message import example ([#8](https://github.com/braintrustdata/braintrust-api-py/issues/8)) ([d896038](https://github.com/braintrustdata/braintrust-api-py/commit/d89603821db91e98295bf10021b04ae09fbeffbe))
* go live ([#15](https://github.com/braintrustdata/braintrust-api-py/issues/15)) ([f58d9a4](https://github.com/braintrustdata/braintrust-api-py/commit/f58d9a40de5985b1c134b91b0ef94365ee0e057e))
* go live ([#17](https://github.com/braintrustdata/braintrust-api-py/issues/17)) ([02c13c9](https://github.com/braintrustdata/braintrust-api-py/commit/02c13c9bdd057cb4cc8b944ecfb396e46ebc78de))
* go live ([#19](https://github.com/braintrustdata/braintrust-api-py/issues/19)) ([e53c510](https://github.com/braintrustdata/braintrust-api-py/commit/e53c510a038cfeb071c9aa24756ea08e9dcfe8f9))
* **internal:** add type construction helper ([#13](https://github.com/braintrustdata/braintrust-api-py/issues/13)) ([a2c4cb4](https://github.com/braintrustdata/braintrust-api-py/commit/a2c4cb448228e8ef18bfaa0978fcc1c933871626))
* **internal:** codegen related update ([#11](https://github.com/braintrustdata/braintrust-api-py/issues/11)) ([a60c6ca](https://github.com/braintrustdata/braintrust-api-py/commit/a60c6cab9a4a009ff0b9c51e0d9c73ee6e6e8366))
* **internal:** codegen related update ([#12](https://github.com/braintrustdata/braintrust-api-py/issues/12)) ([7777daa](https://github.com/braintrustdata/braintrust-api-py/commit/7777daaad919f595c2d5277636446f9514824a93))
* **internal:** codegen related update ([#14](https://github.com/braintrustdata/braintrust-api-py/issues/14)) ([7a16bc0](https://github.com/braintrustdata/braintrust-api-py/commit/7a16bc0420213e34f36bfe124ac65a5f4656f810))
* **internal:** remove deprecated ruff config ([da2e77e](https://github.com/braintrustdata/braintrust-api-py/commit/da2e77e84b2353d240b95637a3596450bf0c234e))

## 0.2.0 (2024-07-23)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.1.0...v0.2.0)

### Features

* **api:** update via SDK Studio ([c4fffb6](https://github.com/braintrustdata/braintrust-api-py/commit/c4fffb6bb272e76e39ff2fe389d70af34fadb9e5))


### Chores

* go live ([#6](https://github.com/braintrustdata/braintrust-api-py/issues/6)) ([14a043a](https://github.com/braintrustdata/braintrust-api-py/commit/14a043a75def8813875602323d1746ad287a8d26))

## 0.1.0 (2024-07-23)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.0.1...v0.1.0)

### Features

* **api:** OpenAPI spec update ([1ca3e96](https://github.com/braintrustdata/braintrust-api-py/commit/1ca3e96ab1a9f32e7b7d0825affe151f51bb4814))
* **api:** OpenAPI spec update ([31d9bb9](https://github.com/braintrustdata/braintrust-api-py/commit/31d9bb94384b0b2267fe6d20fa79d296478e5a8e))
* **api:** OpenAPI spec update ([216d58f](https://github.com/braintrustdata/braintrust-api-py/commit/216d58ff0ec67a6b22629b3ab936c7788e0e36b9))
* **api:** OpenAPI spec update ([88472ba](https://github.com/braintrustdata/braintrust-api-py/commit/88472bab9c2275f4a424447bb8a4a8b5974ea107))
* **api:** OpenAPI spec update ([8c43125](https://github.com/braintrustdata/braintrust-api-py/commit/8c4312568238ff6ce98bb0cab66608663d07349a))
* **api:** OpenAPI spec update ([40715d3](https://github.com/braintrustdata/braintrust-api-py/commit/40715d315729afbe8469033389adcba410bf13f1))
* **api:** OpenAPI spec update ([5177ca1](https://github.com/braintrustdata/braintrust-api-py/commit/5177ca1280fe11aa8a7de553e0a13d70c2c95cf4))
* **api:** OpenAPI spec update ([0162e97](https://github.com/braintrustdata/braintrust-api-py/commit/0162e97c69bf3352cc53ae1e61bd2b4931b2c0d3))
* **api:** OpenAPI spec update ([25ac436](https://github.com/braintrustdata/braintrust-api-py/commit/25ac436ddc6cfa5c6a1e6d022ecbf9efb7deaac8))
* **api:** OpenAPI spec update ([02ab679](https://github.com/braintrustdata/braintrust-api-py/commit/02ab6799c304b96ea2487b7d732a04ec7f3246dc))
* **api:** OpenAPI spec update ([3dd8dfa](https://github.com/braintrustdata/braintrust-api-py/commit/3dd8dfa4f3fc853bd09303014652757129d8fa59))
* **api:** update via SDK Studio ([4ed45cd](https://github.com/braintrustdata/braintrust-api-py/commit/4ed45cdd1ca7ab453d281fad6a9c7a804c0f95ea))
* **api:** update via SDK Studio ([3c8c468](https://github.com/braintrustdata/braintrust-api-py/commit/3c8c4685751e6a5849cad9c0de5870c34342b5e0))
* **api:** update via SDK Studio ([ba29199](https://github.com/braintrustdata/braintrust-api-py/commit/ba291991cfa86ad122ad071c7c46bf3c2d8e8794))
* **api:** update via SDK Studio ([0039e5f](https://github.com/braintrustdata/braintrust-api-py/commit/0039e5f3348666dd9f71b929758182ceb0d293c3))
* **api:** update via SDK Studio ([3b68ad0](https://github.com/braintrustdata/braintrust-api-py/commit/3b68ad0087e8574a623f126b323ae4690e5a0f30))
* **api:** update via SDK Studio ([1c8d22f](https://github.com/braintrustdata/braintrust-api-py/commit/1c8d22ff997f9c03c6dfc6ab4304b75e12cba41f))
* **api:** update via SDK Studio ([28413ef](https://github.com/braintrustdata/braintrust-api-py/commit/28413efe063901d987c9c868184a66aa1ca17637))
* **api:** update via SDK Studio ([4e9c60c](https://github.com/braintrustdata/braintrust-api-py/commit/4e9c60c4fa6856a197d453b538260171c5966242))
* **api:** update via SDK Studio ([b320264](https://github.com/braintrustdata/braintrust-api-py/commit/b3202642d0682fb1257daa261849b0ca04f6f9ca))
* **api:** update via SDK Studio ([cb8908e](https://github.com/braintrustdata/braintrust-api-py/commit/cb8908eb669dfd3dcf62fd46a68c205e79bee4a1))
* **api:** update via SDK Studio ([41dcb5c](https://github.com/braintrustdata/braintrust-api-py/commit/41dcb5cde645062bfceaf9166a1302dd7664187d))
* **api:** update via SDK Studio ([1421b35](https://github.com/braintrustdata/braintrust-api-py/commit/1421b35041a62bd3f2c0024d520d69c8de827f0a))
* **api:** update via SDK Studio ([c0b7781](https://github.com/braintrustdata/braintrust-api-py/commit/c0b7781348679a3e7bba39fc6142b6a8e5f3db9a))
* **api:** update via SDK Studio ([6ffa8c3](https://github.com/braintrustdata/braintrust-api-py/commit/6ffa8c3614ba4cfb4550e4b3301cb9373deecb5d))
* **api:** update via SDK Studio ([21db786](https://github.com/braintrustdata/braintrust-api-py/commit/21db7868697295880a570c98f80c9e3da51755c7))
* **api:** update via SDK Studio ([f706e5a](https://github.com/braintrustdata/braintrust-api-py/commit/f706e5aaf1e2c85a3149d81661045223b11d040e))
* **api:** update via SDK Studio ([959b8ff](https://github.com/braintrustdata/braintrust-api-py/commit/959b8ffd1edd936864809fc44c4d07f7e72e0ec0))
* **api:** update via SDK Studio ([37a92cc](https://github.com/braintrustdata/braintrust-api-py/commit/37a92cc0028d24b74aedf814b97a9eca1e9c0ea2))
* **api:** update via SDK Studio ([7da581d](https://github.com/braintrustdata/braintrust-api-py/commit/7da581d94322e92d458f03beab4fb04f8614b935))
* **api:** update via SDK Studio ([8d0c922](https://github.com/braintrustdata/braintrust-api-py/commit/8d0c922e5bf17df24830da9ed2b280d45015f2f0))
* **api:** update via SDK Studio ([#3](https://github.com/braintrustdata/braintrust-api-py/issues/3)) ([b1886d6](https://github.com/braintrustdata/braintrust-api-py/commit/b1886d615315adb6437d14f675823184c8ad9182))
* OpenAPI spec update ([cb9309c](https://github.com/braintrustdata/braintrust-api-py/commit/cb9309c148e7c7a4b9ac3ca49a41eff87546c44e))
* OpenAPI spec update ([231ac24](https://github.com/braintrustdata/braintrust-api-py/commit/231ac24021e05190d35518080ad2a0e87f5e59f9))
* OpenAPI spec update ([14d3c1e](https://github.com/braintrustdata/braintrust-api-py/commit/14d3c1e80491391f362f4d3543295e03a97f9176))
* OpenAPI spec update ([6c96b0e](https://github.com/braintrustdata/braintrust-api-py/commit/6c96b0e2860aa87036dd4d5e19b2a46e0414a3f3))


### Chores

* **docs:** minor update to formatting of API link in README ([1246537](https://github.com/braintrustdata/braintrust-api-py/commit/1246537c6a36670eef2aac30f4b2b7f3b08f7216))
* go live ([#2](https://github.com/braintrustdata/braintrust-api-py/issues/2)) ([a817ff3](https://github.com/braintrustdata/braintrust-api-py/commit/a817ff308924cb2811bb4c9e488c2d2151a274ba))
* **internal:** codegen related update ([c664419](https://github.com/braintrustdata/braintrust-api-py/commit/c664419e8216f955569471c6eb25dcf3db00e020))
* **internal:** minor options / compat functions updates ([460bdb7](https://github.com/braintrustdata/braintrust-api-py/commit/460bdb7b213112d07b414f3b69fed1ad942641d9))
* update SDK settings ([4360a1f](https://github.com/braintrustdata/braintrust-api-py/commit/4360a1f2fbeab5e2e083c269aeb233c30540f8cc))
