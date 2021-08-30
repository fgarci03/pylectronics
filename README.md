[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<br />
<p align="center">
  <h3 align="center">Pylectronics</h3>

  <p align="center">
    Reproduce digital electronics in Python
    <br />
    <br />
    <a href="https://github.com/fgarci03/pylectronics/issues">Report Bug</a>
    ·
    <a href="https://github.com/fgarci03/pylectronics/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#coding-guidelines">Coding Guidelines</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

This project is an attempt to reproduce digital electronics in Python. Its **ultimate** goal is to be able to build an
actual CPU by simulating the core components of a real, physical, processor (using Transistors to build Logic Gates,
using Logic Gates to build a Half Adder, using Half Adders to build Full Adders, and so on and so forth...).

By adding more components to the project, you will be helping achieve that goal!



## Getting Started

### Prerequisites

Make sure you have [virtualenv](https://virtualenv.pypa.io/) and [Poetry](https://python-poetry.org/) installed.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/fgarci03/pylectronics.git
   ```
2. Create the virtualenv
   ```sh
   virtualenv venv
   ```
3. Use it
   ```sh
   source venv/bin/activate
   ```
4. Install packages
   ```sh
   poetry install
   ```



## Usage

The project is yet in its infancy, so there is not much to show for apart from some components.



## Coding Guidelines

This project uses [Black](https://black.readthedocs.io/), [Prospector](http://prospector.landscape.io/en/master/), and 
[Pytest](https://docs.pytest.org/). It is set to enforce all the linting rules and 100% test coverage when running:
```sh
./run_tests.sh
```



## Roadmap

See the [open issues](https://github.com/fgarci03/pylectronics/issues) for a list of proposed features (and known
issues).

It's tough to provide a real roadmap at this stage, since I'm still learning about digital electronics. Nonetheless,
there are a few concepts that should be thought about to allow the project to grow:

* **Memory**: All computers need memory. Whether D-Type FlipFlops, or SR Latches, we will need these components to build
more complex components...
  * ...such as [registers](https://github.com/fgarci03/pylectronics/issues/2)!
  * Speaking of memory... We need to build the [concept of time](https://github.com/fgarci03/pylectronics/issues/1)!
* **[Unified Interfaces](https://github.com/fgarci03/pylectronics/issues/3)**: It would be nice to have some utilities
baked into all the components that can give us some stats:
  * Number of Transistors in this component
  * Total Number of Transistors,
  * Timing functions to measure performance
  * Etc
* **[and more!](https://github.com/fgarci03/pylectronics/issues)**


## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Do your magic
4. Make sure tests pass with 100% coverage, as well as static validation (`./run_tests.sh`)
5. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the Branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request



## License

Distributed under the MIT License. See `LICENSE` for more information.



## Contact

Filipe Garcia - [https://filipe-garcia.com](https://filipe-garcia.com)

Project Link: [https://github.com/fgarci03/pylectronics](https://github.com/fgarci03/pylectronics)




<!-- MARKDOWN LINKS & IMAGES -->
[forks-shield]: https://img.shields.io/github/forks/fgarci03/pylectronics?style=for-the-badge
[forks-url]: https://github.com/fgarci03/pylectronics/network/members
[stars-shield]: https://img.shields.io/github/stars/fgarci03/pylectronics?style=for-the-badge
[stars-url]: https://github.com/fgarci03/pylectronics/stargazers
[issues-shield]: https://img.shields.io/github/issues/fgarci03/pylectronics?style=for-the-badge
[issues-url]: https://github.com/fgarci03/pylectronics/issues
[license-shield]: https://img.shields.io/github/license/fgarci03/pylectronics?style=for-the-badge
[license-url]: https://github.com/fgarci03/pylectronics/blob/master/LICENSE.txt
