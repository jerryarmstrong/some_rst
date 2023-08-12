components/NotificationsCard/NotifiFullLogo.tsx
===============================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { useTheme } from 'next-themes'
import NotifiLogoFullDark from './NotifiLogoFullDark'
import NotifiLogoFullLight from './NotifiLogoFullLight '

const NotifiFullLogo = ({ height = '23', width = '340' }) => {
  const { theme } = useTheme()
  return theme === 'Dark' ? (
    <NotifiLogoFullLight height={height} width={width} />
  ) : (
    <NotifiLogoFullDark height={height} width={width} />
  )
}

export default NotifiFullLogo


