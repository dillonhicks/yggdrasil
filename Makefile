#
# Tedium Automation Makefile
#

XRM=xargs -I {} rm -fv {}

clean:
	find . | grep ~$$ | $(XRM)
	find . | grep [.]pyc$$ | $(XRM)