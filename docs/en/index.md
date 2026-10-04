---
title: "LEM Primer"
lang: en
translated_from: "56298d2"
translated_on: 2026-10-04
---

# LEM Primer

**The limit equilibrium method, from first principles to how it is used in practice**

The limit equilibrium method (LEM) is the most widely used way to assess the stability of slopes. Yet the factor-of-safety formulas in textbooks rarely show how they are derived, what they assume, and what they do not guarantee.

This primer is for readers who have not studied LEM before. It follows one thread from the stress of continuum mechanics to reading the results of a real analysis. It has three chapters of theory, practice pages that check them in code, and a shared glossary.

```{toctree}
:maxdepth: 1
:hidden:
:caption: Theory

continuum-mechanics-to-lem-start
what-is-limit-equilibrium-method
lem-in-practice-mechanical-perspective
```

```{toctree}
:maxdepth: 1
:hidden:
:caption: Practice

practice-infinite-slope
practice-slices-2d
practice-columns-3d
```

```{toctree}
:maxdepth: 1
:hidden:
:caption: Appendix

lem-glossary
```

## Theory

::::{grid} 1
:gutter: 2

:::{grid-item-card} Chapter 1: From continuum mechanics to where the limit equilibrium method begins
:link: continuum-mechanics-to-lem-start
:link-type: doc

How do stress and a failure criterion become the forces on a slice base?
:::

:::{grid-item-card} Chapter 2: What is the limit equilibrium method?
:link: what-is-limit-equilibrium-method
:link-type: doc

What assumptions does each method use to determine the remaining unknowns?
:::

:::{grid-item-card} Chapter 3: Using the limit equilibrium method in practice
:link: lem-in-practice-mechanical-perspective
:link-type: doc

How should slip surfaces other than circles, the direction of sliding, and discretization be read?
:::

::::

The theory is meant to be read in order, from Chapter 1. Each chapter has a main text and collapsed supplements, which hold the details of derivations and sign conventions. The terms and symbols are collected in the [Glossary](lem-glossary.md).

## Practice

::::{grid} 1
:gutter: 2

:::{grid-item-card} Practice 1: Computing the factor of safety of an infinite slope
:link: practice-infinite-slope
:link-type: doc

Computes the factor of safety of an infinite slope, starting from splitting the traction
:::

:::{grid-item-card} Practice 2: Computing the factor of safety of a circular slip with the method of slices
:link: practice-slices-2d
:link-type: doc

Computes, for one circle, the factors of safety of four methods and the equilibrium residuals
:::

:::{grid-item-card} Practice 3: Computing the factor of safety of a 3D slip surface with the method of columns
:link: practice-columns-3d
:link-type: doc

Builds a column table for an ellipsoidal slip surface and computes the 3D factor of safety
:::

::::

The practice pages write the code in Python and NumPy, and check the equations and ideas of the theory with numbers. The values of Practice 2 and Practice 3 are each checked against the values of the practice before it, for example by reducing a plane slip surface to the infinite slope. Practice 1 can be started after Chapter 1; Practice 2 and Practice 3 are best taken after Chapter 3.

## About this primer

This primer is a general introduction to LEM that depends on no particular analysis software. One implementation is the slope stability code [LEM Lab](https://github.com/ibaraki-kozo-lab/lem-lab).
