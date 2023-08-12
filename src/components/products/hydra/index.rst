src/components/products/hydra/index.js
======================================

Last edited: 2023-08-11 10:00:06

Contents:

.. code-block:: js

    import {
  changelogSection,
  documentationSection,
  recipesSection,
  referencesSection,
} from '@/shared/sections'
import { Hero } from './Hero'
import { Logo } from './Logo'

export const hydra = {
  name: 'Hydra',
  headline: 'Fanout wallets',
  description: 'Create shared wallets, split between multiple shareholders.',
  path: 'hydra',
  logo: Logo,
  github: 'https://github.com/metaplex-foundation/mpl-hydra',
  className: 'accent-amber',
  heroes: [{ path: '/hydra', component: Hero }],
  sections: [
    {
      ...documentationSection('hydra'),
      navigation: [
        {
          title: 'Introduction',
          links: [
            { title: 'Overview', href: '/hydra' },
            { title: 'Getting started', href: '/hydra/getting-started' },
          ],
        },
      ],
    },
    { ...referencesSection('hydra') },
    { ...recipesSection('hydra') },
    { ...changelogSection('hydra') },
  ],
}


