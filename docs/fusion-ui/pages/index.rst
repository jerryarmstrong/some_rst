pages/index.tsx
===============

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: tsx

    import type { NextPage } from 'next'
import { List, ListItem } from "@mui/material"
import Head from 'next/head'
import styles from '../styles/Home.module.css'
import Link from 'next/link'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Fusion UI</title>
        <meta name="description" content="Fusion UI" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <List>
        <ListItem>
          <Link href="/constraints" >Create A Constraint Model</Link>
        </ListItem>
        <ListItem>
          <Link href="/trifle" >Create A Token-Owned Escrow</Link>
        </ListItem>
        <ListItem>
          <Link href="/setup" >Set up example NFTs</Link>
        </ListItem>
      </List>
    </div>
  )
}

export default Home


