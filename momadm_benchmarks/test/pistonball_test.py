"""Test the multi-objective pistonball environment."""

from momadm_benchmarks.envs.mo_pistonball import mo_pistonball_v0


env = mo_pistonball_v0.env(
    n_pistons=20,
    time_penalty=-0.1,
    continuous=True,
    random_drop=True,
    random_rotate=True,
    ball_mass=0.75,
    ball_friction=0.3,
    ball_elasticity=1.5,
    max_cycles=125,
    render_mode="human",
)
env.reset(seed=42)

# Sample random actions for each agent and run the environment.
for agent in env.agents:
    observation, reward, termination, truncation, info = env.last()
    action = env.action_space(agent).sample()
    env.step(action)

# Close the environment
env.close()
