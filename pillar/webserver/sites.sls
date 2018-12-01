#   -------------------------------------------------------------
#   Salt — Web server configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Woods Clouds
#   Created:        2018-12-01
#   License:        Trivial work, not eligible to copyright
#   -------------------------------------------------------------

#   -------------------------------------------------------------
#   Table of contents
#   -------------------------------------------------------------
#
#   :: Domains by forest
#   :: Sites by forest
#
#   -------------------------------------------------------------

#   -------------------------------------------------------------
#   Domains by forest
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

webserver_domains:
  woodscloud-web:
    - woodscloud.com

#   -------------------------------------------------------------
#   Sites by forest
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

webserver_sites:
  woodscloud-web:
    www.woodscloud.com: {}
