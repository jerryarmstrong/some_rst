components/NotifiIcon.tsx
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { useTheme } from 'next-themes'
import NotifiIconDark from './NotificationsSwitch/NotifiIconDark'
import NotifiIconLight from './NotificationsSwitch/NotifiIconLight'

const NotifiIcon = ({ height = '30' }) => {
  const { theme } = useTheme()
  return theme === 'Dark' ? (
    <NotifiIconLight height={height} width={height} />
  ) : (
    <NotifiIconDark height={height} width={height} />
  )
}

export default NotifiIcon


