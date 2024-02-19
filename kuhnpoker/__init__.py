from gymnasium.envs.registration import register

register(
    id="kuhnpoker/KuhnPoker-v0",
    entry_point="kuhnpoker.envs:KuhnPokerEnv",
    nondeterministic=True
)
