# this file will simply navigate back to the walmart home page
# for use when errors occur

#this xpath may only click on the mobile app button which is invisable while on desktop. Need to test
xp_homepage = "//a[contains(@aria-label, 'Walmart Homepage')]"
#back up xpath, issue is the link id is not clear as to where it goes. This might be changed.
xp_homepage_link_id ="//a[contains(@link-identifier, 'Desktop')]"

