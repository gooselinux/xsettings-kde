#/bin/sh

DATE=$(date +%Y%m%d)
MODULE="$(basename $0 -svn_checkout.sh)"
SVNROOT=http://svn.mandriva.com/svn/soft/theme/xsettings-kde/tags/V0_11_1mdv/

set -x
rm -rf $MODULE

svn export $SVNROOT $MODULE

## tar it up
tar cjf $MODULE-${DATE}svn.tar.bz2 $MODULE

## cleanup
rm -rf $MODULE

