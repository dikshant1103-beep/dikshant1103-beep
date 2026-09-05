# Dikshant

**Curious Enough To Question. Stubborn Enough To Build.**

Mechanical design engineer, M.Tech in CAD/CAM. I design machines, then build
the physics to prove them — which in practice means most of my projects start
in CAD and end as a simulator, a solver, or a piece of software that tells me
whether the design actually works.

Right now I'm teaching myself the rest of the stack — controls, embedded, and
machine learning — so I can take a robot from geometry to hardware without
handing off the parts I don't understand.

## Selected work

<!-- WORK:START -->
| Project | | Built with | Last push |
|---|---|---|---|
| **[Chassis Workbench](https://github.com/dikshant1103-beep/chassis-workbench)** · [live](https://chassis-workbench.vercel.app) | Motorcycle chassis and suspension design — geometry, kinematics, multibody dynamics with a generalized-α solver, structural concept lane | TypeScript | Aug 2026 |
| **[moto_sim](https://github.com/dikshant1103-beep/moto-sim)** | PyChrono motorcycle simulator — tire PINNs, ROS2/Gazebo digital twin, validated against the Whipple benchmark to 0.02% | Python | Aug 2026 |
| **[WarrantyLens](https://github.com/dikshant1103-beep/warrantylens)** | EV warranty inspection assistant. Vision, OCR and retrieval over claim evidence — advisory and human-in-the-loop, it never calls fraud on its own | Python | Jul 2026 |
| **[MambaRUL Studio](https://github.com/dikshant1103-beep/mambarul-studio)** | Battery remaining-useful-life prediction with Mamba state-space models, conformal intervals, shipped as a desktop app | TypeScript | Jul 2026 |
| **[EV Drone Inspector](https://github.com/dikshant1103-beep/drone-inspector)** | Autonomous warehouse inspection — PX4 SITL, Gazebo, ROS2, and a control centre with waypoint planning and click-to-go | Python | Jul 2026 |
| **[Jarvis](https://github.com/dikshant1103-beep/jarvis)** | A study assistant that runs entirely on a 4 GB laptop GPU. Grounds its answers in real APIs rather than model recall | Python | Jul 2026 |
| **[Zero → Robot](https://github.com/dikshant1103-beep/zero-to-robot)** · [live](https://zerotorobot.vercel.app) | The curriculum above, as a dashboard I actually use | JavaScript | Jul 2026 |

<sub>Table regenerated from the GitHub API — last run 31 Aug 2026.</sub>
<!-- WORK:END -->

More, including the mechanical and CAD work: **[dikshant1103-beep.github.io](https://dikshant1103-beep.github.io)**

## What I'm working on

**Battery layout as a stability parameter.** An electric motorcycle's pack is about a quarter of its
mass, and unlike an engine you can split it and put the pieces where you like. The placement
literature is inherited from cars and argues about the centre of gravity. It turns out that if you
hold total mass *and* CG fixed and only move the modules around, the machine's weave damping still
changes — and the axis that matters is roll, not yaw, by about an order of magnitude. Two layouts
that are mirror images of each other, identical in mass, CG and both principal inertias, differ
sevenfold; the sign of the product of inertia decides it.

Paper drafted for *Vehicle System Dynamics*. It is simulation work with no vehicle behind it yet, so
the prediction is written to be falsifiable: any motorcycle, 50 kg of ballast, 300 m of closed
straight, one test day. The model is verified four ways before it is believed — against the published
Meijaard benchmark, against a second derivation sharing no algebra with the first, by limiting-case
reduction, and against structural claims published by people who had never heard of the work.

Alongside that: a drone I build in hardware and a humanoid I keep in simulation until the hardware is
worth buying. The honest constraint is a GTX 1650 Ti, so everything above is sized to run on a
laptop — which turns out to be a useful discipline rather than only a limitation.

## Reach me

[Portfolio](https://dikshant1103-beep.github.io) · [LinkedIn](https://www.linkedin.com/in/dikshant-470b7618b/) · dikshant1103@gmail.com
