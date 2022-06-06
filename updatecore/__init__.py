# This init is required for each cog.
# Import your main class from the cog's folder.
from .updatecore import updatecore


def setup(bot):
    bot.add_cog(updatecore(bot))
