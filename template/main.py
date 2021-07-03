from redbot.core import commands
import subprocess
import redis

r = redis.Redis(
    host='localhost')



# Classname should be CamelCase and the same spelling as the folder
class Template(commands.Cog):
    """Description of cog"""

    @commands.command()
    async def pull(self, ctx):
        """Pull smth from Redis"""
        subprocess.run(["php", "pull.php"])
        pull = r.get("pull")
        await ctx.send(pull)

    @commands.command()
    async def push(self, ctx):
        """Push smth to Redis"""
        subprocess.run(["php", "push.php"])
        push = r.get("push")
        await ctx.send(push)