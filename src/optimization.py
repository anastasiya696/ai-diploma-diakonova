from src.functions import loss_function
from src.derivatives import loss_derivative


def gradient_descent(start_x, learning_rate, steps):
    x_current = start_x
    history = []

    for step in range(steps):
        loss = loss_function(x_current)
        grad = loss_derivative(x_current)

        history.append({
            "step": step,
            "x": x_current,
            "loss": loss,
            "derivative": grad
        })

        x_current = x_current - learning_rate * grad

    return history