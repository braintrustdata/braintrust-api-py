# Changelog

## 0.7.0 (2025-08-21)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/braintrustdata/braintrust-api-py/compare/v0.6.0...v0.7.0)

### Features

* **api:** manual updates ([#118](https://github.com/braintrustdata/braintrust-api-py/issues/118)) ([e06c7c2](https://github.com/braintrustdata/braintrust-api-py/commit/e06c7c2d2a365e6e59c885358485bdfa1413bc40))
* **api:** manual updates ([#119](https://github.com/braintrustdata/braintrust-api-py/issues/119)) ([e37a8c1](https://github.com/braintrustdata/braintrust-api-py/commit/e37a8c1b81f31ea4795150dae1ce1a92474b6b6f))
* **api:** manual updates ([#120](https://github.com/braintrustdata/braintrust-api-py/issues/120)) ([bcf8542](https://github.com/braintrustdata/braintrust-api-py/commit/bcf854293c2afc6d093ccdb84a9eb8d397f5831e))
* clean up environment call outs ([417b455](https://github.com/braintrustdata/braintrust-api-py/commit/417b455756e30f8f9ecd3b1077bbaf74441223e3))
* **client:** add follow_redirects request option ([0cc0671](https://github.com/braintrustdata/braintrust-api-py/commit/0cc0671a2cb5fe858ddac2d58ee73c30b51fe7c0))
* **client:** add support for aiohttp ([ba244c1](https://github.com/braintrustdata/braintrust-api-py/commit/ba244c167e9f23e8eb6901e336b378848e32f26d))
* **client:** allow passing `NotGiven` for body ([#109](https://github.com/braintrustdata/braintrust-api-py/issues/109)) ([731a3a1](https://github.com/braintrustdata/braintrust-api-py/commit/731a3a13b3f1cad4e5211684078f020487262076))
* **client:** send `X-Stainless-Read-Timeout` header ([#104](https://github.com/braintrustdata/braintrust-api-py/issues/104)) ([a81d0cb](https://github.com/braintrustdata/braintrust-api-py/commit/a81d0cb7af62e5cbcf4a7492652e873737575afc))
* **client:** support file upload requests ([acc97c4](https://github.com/braintrustdata/braintrust-api-py/commit/acc97c4f2c6d5da0620c8839f104fc079d554525))


### Bug Fixes

* **api:** better support union schemas with common properties ([#92](https://github.com/braintrustdata/braintrust-api-py/issues/92)) ([12e53c2](https://github.com/braintrustdata/braintrust-api-py/commit/12e53c2d042af021874740c0442d1dd8f691e68d))
* asyncify on non-asyncio runtimes ([#108](https://github.com/braintrustdata/braintrust-api-py/issues/108)) ([2cd0b7e](https://github.com/braintrustdata/braintrust-api-py/commit/2cd0b7eadcef42310cdaaab88e261661baf66e07))
* **ci:** correct conditional ([d19dd17](https://github.com/braintrustdata/braintrust-api-py/commit/d19dd1785e16742903977db39903cf2ec9b51ca7))
* **ci:** ensure pip is always available ([#123](https://github.com/braintrustdata/braintrust-api-py/issues/123)) ([62dff95](https://github.com/braintrustdata/braintrust-api-py/commit/62dff9577d3888dfbcb811a1d95f2d19950711e7))
* **ci:** release-doctor — report correct token name ([995ef19](https://github.com/braintrustdata/braintrust-api-py/commit/995ef19183a9262a29b199b9b683ed38cbaaad6e))
* **ci:** remove publishing patch ([#124](https://github.com/braintrustdata/braintrust-api-py/issues/124)) ([e0320a6](https://github.com/braintrustdata/braintrust-api-py/commit/e0320a6eb1d40e8d15453d97ed53ccd5e4ec87cd))
* **client:** correctly parse binary response | stream ([4c88e34](https://github.com/braintrustdata/braintrust-api-py/commit/4c88e34fdb52be50d568cf4fb029e2f9eb1576d9))
* **client:** don't send Content-Type header on GET requests ([c14589e](https://github.com/braintrustdata/braintrust-api-py/commit/c14589e7d3147acdd6880eb81c9db217372acff1))
* **client:** mark some request bodies as optional ([731a3a1](https://github.com/braintrustdata/braintrust-api-py/commit/731a3a13b3f1cad4e5211684078f020487262076))
* **client:** only call .close() when needed ([#89](https://github.com/braintrustdata/braintrust-api-py/issues/89)) ([b17e41e](https://github.com/braintrustdata/braintrust-api-py/commit/b17e41e01a865ecce9fb7dd53fe0e454ee831a91))
* correctly handle deserialising `cls` fields ([#94](https://github.com/braintrustdata/braintrust-api-py/issues/94)) ([72ebbe1](https://github.com/braintrustdata/braintrust-api-py/commit/72ebbe1fb979d13e557b5728b914ec07c59c307a))
* **docs/api:** remove references to nonexistent types ([afcbfa9](https://github.com/braintrustdata/braintrust-api-py/commit/afcbfa9c99c2cf5e8bc189b23e7c17eac4ddd5b9))
* **package:** support direct resource imports ([b14060f](https://github.com/braintrustdata/braintrust-api-py/commit/b14060f4bfe687f593518165d5c7ab8e1f0ea748))
* **parsing:** correctly handle nested discriminated unions ([42d4555](https://github.com/braintrustdata/braintrust-api-py/commit/42d4555fed03b08b56a1d912c172678867d71f3e))
* **parsing:** ignore empty metadata ([d638c8a](https://github.com/braintrustdata/braintrust-api-py/commit/d638c8a10c38a3a7797d33f226513fcbc6d2c4fe))
* **parsing:** parse extra field types ([3919097](https://github.com/braintrustdata/braintrust-api-py/commit/391909714851975cd80d3d8b750b544c069375a3))
* **perf:** optimize some hot paths ([8aa7193](https://github.com/braintrustdata/braintrust-api-py/commit/8aa71935dbdb15e65aa50ea14eabd1f5ae27524e))
* **perf:** skip traversing types for NotGiven values ([cdf262b](https://github.com/braintrustdata/braintrust-api-py/commit/cdf262bf241b311addbbac638b97b99bf5038f46))
* **pydantic v1:** more robust ModelField.annotation check ([640f98b](https://github.com/braintrustdata/braintrust-api-py/commit/640f98bf04edb7148d4e217dffe7f20d403185fa))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([88c2693](https://github.com/braintrustdata/braintrust-api-py/commit/88c2693a55688606dbb505f82acc144673c3474c))
* **tests:** make test_get_platform less flaky ([#97](https://github.com/braintrustdata/braintrust-api-py/issues/97)) ([539f898](https://github.com/braintrustdata/braintrust-api-py/commit/539f898c0ef3bd3b97889a6f25debd058fbbb0b0))
* **types:** add missing total=False ([#126](https://github.com/braintrustdata/braintrust-api-py/issues/126)) ([74ea3e8](https://github.com/braintrustdata/braintrust-api-py/commit/74ea3e86731ebd651f4051865a636f06b16998d3))
* **types:** handle more discriminated union shapes ([#122](https://github.com/braintrustdata/braintrust-api-py/issues/122)) ([fcf590f](https://github.com/braintrustdata/braintrust-api-py/commit/fcf590f9015ed87e8c52661460535f3cf38a8ac0))


### Chores

* add missing isclass check ([#87](https://github.com/braintrustdata/braintrust-api-py/issues/87)) ([bfb504b](https://github.com/braintrustdata/braintrust-api-py/commit/bfb504b89946d937964fa6b11ad9ec759f44ca5f))
* broadly detect json family of content-type headers ([eb1c4af](https://github.com/braintrustdata/braintrust-api-py/commit/eb1c4af14b0c59330ac2abf8b948d26f3991189c))
* **ci:** add timeout thresholds for CI jobs ([8eb40d8](https://github.com/braintrustdata/braintrust-api-py/commit/8eb40d826eebb275e0c6d23cade9accbe94fe729))
* **ci:** change upload type ([b47294f](https://github.com/braintrustdata/braintrust-api-py/commit/b47294f9ca752f38fecdc305ec50979251abc29a))
* **ci:** enable for pull requests ([df18cbc](https://github.com/braintrustdata/braintrust-api-py/commit/df18cbcd15b0df7c51472f29445fe26aac44f095))
* **ci:** fix installation instructions ([8aa8c86](https://github.com/braintrustdata/braintrust-api-py/commit/8aa8c861b4914dc2fbf935591c7d6f1cd8498e89))
* **ci:** only run for pushes and fork pull requests ([66accc5](https://github.com/braintrustdata/braintrust-api-py/commit/66accc56aa4d5b1f453416986c058a9a7c7b8ee3))
* **ci:** only use depot for staging repos ([3740879](https://github.com/braintrustdata/braintrust-api-py/commit/3740879ac2684ca7a65a6ba828dee58bcc3230a0))
* **ci:** upload sdks to package manager ([28aed61](https://github.com/braintrustdata/braintrust-api-py/commit/28aed610cacb5a18f5769af481417ba4c7a0ae29))
* **client:** minor internal fixes ([fa4d5c4](https://github.com/braintrustdata/braintrust-api-py/commit/fa4d5c402e177ad66b99927daec35a5879edb35d))
* **client:** simplify `Optional[object]` to just `object` ([#86](https://github.com/braintrustdata/braintrust-api-py/issues/86)) ([edc7ec8](https://github.com/braintrustdata/braintrust-api-py/commit/edc7ec8b753f0966b0dc46fbf67889d5600ebf12))
* **docs:** grammar improvements ([528aa41](https://github.com/braintrustdata/braintrust-api-py/commit/528aa419d4cd2778c82b10b6b494fc8d20abc00b))
* **docs:** remove reference to rye shell ([2dc42f9](https://github.com/braintrustdata/braintrust-api-py/commit/2dc42f90be58606b9ae8a7a58e5be1e549279c37))
* **docs:** remove unnecessary param examples ([c84e8b0](https://github.com/braintrustdata/braintrust-api-py/commit/c84e8b0a7e0e9bf8def132c996b98606c0a2dec3))
* **docs:** update client docstring ([#113](https://github.com/braintrustdata/braintrust-api-py/issues/113)) ([ef563e2](https://github.com/braintrustdata/braintrust-api-py/commit/ef563e21b1746f8836b218626d65e92b7bfb62e4))
* fix typos ([#125](https://github.com/braintrustdata/braintrust-api-py/issues/125)) ([15f7e02](https://github.com/braintrustdata/braintrust-api-py/commit/15f7e0208fc481b67bad494d393c7d364574c514))
* **internal:** avoid errors for isinstance checks on proxies ([dcde56a](https://github.com/braintrustdata/braintrust-api-py/commit/dcde56ab1f270935868e289287141ad5891ac0e5))
* **internal:** avoid pytest-asyncio deprecation warning ([#98](https://github.com/braintrustdata/braintrust-api-py/issues/98)) ([58f4215](https://github.com/braintrustdata/braintrust-api-py/commit/58f4215a46c8acb0676defb807ef1bb2dbd5888b))
* **internal:** base client updates ([ab8ab97](https://github.com/braintrustdata/braintrust-api-py/commit/ab8ab979c40c40b7c1cc97fd65dcf10f29af5d02))
* **internal:** bummp ruff dependency ([#103](https://github.com/braintrustdata/braintrust-api-py/issues/103)) ([704af11](https://github.com/braintrustdata/braintrust-api-py/commit/704af11b4f64bbdf5ec673c20bfb3ddbae4fee66))
* **internal:** bump httpx dependency ([#88](https://github.com/braintrustdata/braintrust-api-py/issues/88)) ([f37b2d0](https://github.com/braintrustdata/braintrust-api-py/commit/f37b2d035467e512ecc0676a2b1643b0fcbb1f4f))
* **internal:** bump pinned h11 dep ([247ddea](https://github.com/braintrustdata/braintrust-api-py/commit/247ddea3d6fa59d70ab595930d0a7ace18d66a0b))
* **internal:** bump pydantic dependency ([#75](https://github.com/braintrustdata/braintrust-api-py/issues/75)) ([cee4d9d](https://github.com/braintrustdata/braintrust-api-py/commit/cee4d9d69b1cd28992af885f09392757af3e9859))
* **internal:** bump pyright version ([019fea9](https://github.com/braintrustdata/braintrust-api-py/commit/019fea9772ccb410b2b8c624854037b2c63352b2))
* **internal:** bump rye to 0.44.0 ([#121](https://github.com/braintrustdata/braintrust-api-py/issues/121)) ([97b0d81](https://github.com/braintrustdata/braintrust-api-py/commit/97b0d817a4909467cff0caaf143411bf5d904434))
* **internal:** change default timeout to an int ([#102](https://github.com/braintrustdata/braintrust-api-py/issues/102)) ([02ff898](https://github.com/braintrustdata/braintrust-api-py/commit/02ff898796501d1baf9b7f79113796f7d61ef9e6))
* **internal:** codegen related update ([d799db4](https://github.com/braintrustdata/braintrust-api-py/commit/d799db49629fed1ad02fabd1bfb428f32f0b88fa))
* **internal:** codegen related update ([0a80ffd](https://github.com/braintrustdata/braintrust-api-py/commit/0a80ffd780ef8d3b4fa4227d5259799f9811740a))
* **internal:** codegen related update ([#101](https://github.com/braintrustdata/braintrust-api-py/issues/101)) ([74c72a3](https://github.com/braintrustdata/braintrust-api-py/commit/74c72a341c219b85a081bf4606a6caf0eac117ba))
* **internal:** codegen related update ([#72](https://github.com/braintrustdata/braintrust-api-py/issues/72)) ([c8d3baf](https://github.com/braintrustdata/braintrust-api-py/commit/c8d3baf536473fc7b2d85e39ce8a498228c03bea))
* **internal:** codegen related update ([#77](https://github.com/braintrustdata/braintrust-api-py/issues/77)) ([e6d7e6d](https://github.com/braintrustdata/braintrust-api-py/commit/e6d7e6d31b02f43cb1a6b83ed78482c73e99567d))
* **internal:** codegen related update ([#78](https://github.com/braintrustdata/braintrust-api-py/issues/78)) ([3805a84](https://github.com/braintrustdata/braintrust-api-py/commit/3805a841cf5e78904c2e25984a13d948b8cdf12f))
* **internal:** codegen related update ([#79](https://github.com/braintrustdata/braintrust-api-py/issues/79)) ([d02caf0](https://github.com/braintrustdata/braintrust-api-py/commit/d02caf0bd34c711cec98358243b6b370eb78edf7))
* **internal:** codegen related update ([#81](https://github.com/braintrustdata/braintrust-api-py/issues/81)) ([0f9e170](https://github.com/braintrustdata/braintrust-api-py/commit/0f9e17051ea65e878c5a02de502e80a292918294))
* **internal:** codegen related update ([#82](https://github.com/braintrustdata/braintrust-api-py/issues/82)) ([c62a02c](https://github.com/braintrustdata/braintrust-api-py/commit/c62a02cb45f7191c6058e5d667499228918351db))
* **internal:** codegen related update ([#85](https://github.com/braintrustdata/braintrust-api-py/issues/85)) ([04d214e](https://github.com/braintrustdata/braintrust-api-py/commit/04d214e0ba25d375fc3c816f68bad370e0b0b63d))
* **internal:** codegen related update ([#91](https://github.com/braintrustdata/braintrust-api-py/issues/91)) ([f4ff2a9](https://github.com/braintrustdata/braintrust-api-py/commit/f4ff2a98ab561f6e4e03a78ee358af17f7a27132))
* **internal:** codegen related update ([#95](https://github.com/braintrustdata/braintrust-api-py/issues/95)) ([2a4460a](https://github.com/braintrustdata/braintrust-api-py/commit/2a4460a7446ed72b958ee1f5257effe850a1802d))
* **internal:** expand CI branch coverage ([a3a2656](https://github.com/braintrustdata/braintrust-api-py/commit/a3a265646ff09013b603bffb3b7358590b112fd0))
* **internal:** fix devcontainers setup ([#110](https://github.com/braintrustdata/braintrust-api-py/issues/110)) ([d782782](https://github.com/braintrustdata/braintrust-api-py/commit/d78278233d819b0ae3d2ebfb16eae38b522f9771))
* **internal:** fix list file params ([b6639ab](https://github.com/braintrustdata/braintrust-api-py/commit/b6639abffec648d42b94373c98d5a889a62aae22))
* **internal:** fix ruff target version ([2e44f60](https://github.com/braintrustdata/braintrust-api-py/commit/2e44f60d9a893d3d0b23a47c92499e4dc24390ed))
* **internal:** fix some typos ([#84](https://github.com/braintrustdata/braintrust-api-py/issues/84)) ([1afb368](https://github.com/braintrustdata/braintrust-api-py/commit/1afb368da87a73c1df3db45c758c7d50827daf27))
* **internal:** fix type traversing dictionary params ([#105](https://github.com/braintrustdata/braintrust-api-py/issues/105)) ([46076eb](https://github.com/braintrustdata/braintrust-api-py/commit/46076ebb88673834f48110408883fb5387a94c47))
* **internal:** import reformatting ([dbac172](https://github.com/braintrustdata/braintrust-api-py/commit/dbac172106ee60ea78d749d974557cc9ff90d891))
* **internal:** minor formatting changes ([77de939](https://github.com/braintrustdata/braintrust-api-py/commit/77de9399a9ff9e2b98359f590cf806ae2f6da11e))
* **internal:** minor formatting changes ([#100](https://github.com/braintrustdata/braintrust-api-py/issues/100)) ([ff3d099](https://github.com/braintrustdata/braintrust-api-py/commit/ff3d099982eecfafda24f00ed8fbe3d3fd7b5162))
* **internal:** minor style changes ([#99](https://github.com/braintrustdata/braintrust-api-py/issues/99)) ([b40d0f4](https://github.com/braintrustdata/braintrust-api-py/commit/b40d0f4efd5aba49466a07567158aefeead39614))
* **internal:** minor type handling changes ([#106](https://github.com/braintrustdata/braintrust-api-py/issues/106)) ([2c42ae6](https://github.com/braintrustdata/braintrust-api-py/commit/2c42ae6dec7232ff806c0320840ffdd2036fc543))
* **internal:** properly set __pydantic_private__ ([#111](https://github.com/braintrustdata/braintrust-api-py/issues/111)) ([0cde4b1](https://github.com/braintrustdata/braintrust-api-py/commit/0cde4b1f436edc303aec5a3ac8e68899c84fa02a))
* **internal:** reduce CI branch coverage ([1997d9b](https://github.com/braintrustdata/braintrust-api-py/commit/1997d9b5d408d96d2fae5d8d1b8d565250ea4690))
* **internal:** refactor retries to not use recursion ([9105502](https://github.com/braintrustdata/braintrust-api-py/commit/9105502535ea87fe89eb43173da10b0ecaa7f9cc))
* **internal:** remove extra empty newlines ([#117](https://github.com/braintrustdata/braintrust-api-py/issues/117)) ([10305c5](https://github.com/braintrustdata/braintrust-api-py/commit/10305c5c85a0767ba4cc9c6f12b5df2c0b850a3e))
* **internal:** remove trailing character ([#127](https://github.com/braintrustdata/braintrust-api-py/issues/127)) ([e49928a](https://github.com/braintrustdata/braintrust-api-py/commit/e49928a4e121ece341f97140c49654992b356e3e))
* **internal:** remove unused http client options forwarding ([#114](https://github.com/braintrustdata/braintrust-api-py/issues/114)) ([0a60d39](https://github.com/braintrustdata/braintrust-api-py/commit/0a60d3912df8fd72902d9467742f75b9b43ab7e1))
* **internal:** slight transform perf improvement ([#128](https://github.com/braintrustdata/braintrust-api-py/issues/128)) ([7254708](https://github.com/braintrustdata/braintrust-api-py/commit/7254708f928fd60b5c211af8fc92b5fb3498e2bf))
* **internal:** update client tests ([#107](https://github.com/braintrustdata/braintrust-api-py/issues/107)) ([ef75a36](https://github.com/braintrustdata/braintrust-api-py/commit/ef75a36384ab8f0a9d2db94af5df59f8387991e0))
* **internal:** update comment in script ([5265934](https://github.com/braintrustdata/braintrust-api-py/commit/52659346bb0ca97bc0695db70e94a4db5c8c70a9))
* **internal:** update conftest.py ([1ddcec1](https://github.com/braintrustdata/braintrust-api-py/commit/1ddcec17a86d389b12546a8f13880146f7180d6b))
* **internal:** update models test ([e33fb48](https://github.com/braintrustdata/braintrust-api-py/commit/e33fb48b58e327e3ad908e926cd4104e10e360f0))
* **internal:** update pyright settings ([279561f](https://github.com/braintrustdata/braintrust-api-py/commit/279561f0479b4133dec3c182a59ccce3e30ed7d1))
* **internal:** updated imports ([#80](https://github.com/braintrustdata/braintrust-api-py/issues/80)) ([3bc669f](https://github.com/braintrustdata/braintrust-api-py/commit/3bc669fe9661325e0d10f94a89f982afecbea043))
* make the `Omit` type public ([#74](https://github.com/braintrustdata/braintrust-api-py/issues/74)) ([e5ea14a](https://github.com/braintrustdata/braintrust-api-py/commit/e5ea14afcd44cb9562c9c0ccc557bbee5531f685))
* **package:** mark python 3.13 as supported ([de2e712](https://github.com/braintrustdata/braintrust-api-py/commit/de2e712b28bb789d652ca065c8027361f17a7419))
* **project:** add settings file for vscode ([85b1443](https://github.com/braintrustdata/braintrust-api-py/commit/85b1443c91c4319040d05a0f76c0d9b8d2969974))
* **readme:** fix version rendering on pypi ([ef96b89](https://github.com/braintrustdata/braintrust-api-py/commit/ef96b89d739a76123cc9a85b53351551418ce367))
* **readme:** update badges ([ccbde54](https://github.com/braintrustdata/braintrust-api-py/commit/ccbde542e7d2006cc451fc5a842c7637b53d3074))
* **tests:** add tests for httpx client instantiation & proxies ([7efaa66](https://github.com/braintrustdata/braintrust-api-py/commit/7efaa66ceb0e2551b389c5387a6acddae34a4ee4))
* **tests:** run tests in parallel ([fc46eeb](https://github.com/braintrustdata/braintrust-api-py/commit/fc46eeb92ce2594de56045767f0b2958452da5eb))
* **tests:** skip some failing tests on the latest python versions ([531820c](https://github.com/braintrustdata/braintrust-api-py/commit/531820c7dff5bf01ce4c895b379d657bc0cad80f))
* update @stainless-api/prism-cli to v5.15.0 ([88496ac](https://github.com/braintrustdata/braintrust-api-py/commit/88496ac37f25d55337ab5364508a7f244b9c66f1))
* update github action ([7cd38ba](https://github.com/braintrustdata/braintrust-api-py/commit/7cd38ba7ddaa2ca938b185d3bc798f13405659d7))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([29b2ac8](https://github.com/braintrustdata/braintrust-api-py/commit/29b2ac8177ee1c7fb71398fc8586036c655a2a2b))
* fix typos ([#90](https://github.com/braintrustdata/braintrust-api-py/issues/90)) ([d717022](https://github.com/braintrustdata/braintrust-api-py/commit/d717022b9e153a081f750b2d4aa30bf1a9ec25b6))
* **raw responses:** fix duplicate `the` ([#96](https://github.com/braintrustdata/braintrust-api-py/issues/96)) ([2af70ba](https://github.com/braintrustdata/braintrust-api-py/commit/2af70ba015d6b0f7bc70586b29f651514001784b))
* **readme:** example snippet for client context manager ([#83](https://github.com/braintrustdata/braintrust-api-py/issues/83)) ([d38014d](https://github.com/braintrustdata/braintrust-api-py/commit/d38014dcb54bc8a869f0ddc4afc987cd46e8f659))
* **readme:** fix http client proxies example ([#76](https://github.com/braintrustdata/braintrust-api-py/issues/76)) ([eebb262](https://github.com/braintrustdata/braintrust-api-py/commit/eebb2621dc7c847f3ab458ef9292269df342ab04))
* revise readme docs about nested params ([#115](https://github.com/braintrustdata/braintrust-api-py/issues/115)) ([c372084](https://github.com/braintrustdata/braintrust-api-py/commit/c372084db61445d20d918aaa44b036480ea60020))
* update URLs from stainlessapi.com to stainless.com ([#112](https://github.com/braintrustdata/braintrust-api-py/issues/112)) ([f369b75](https://github.com/braintrustdata/braintrust-api-py/commit/f369b750d0de33ac22a20fa6b525b242987627b1))

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
