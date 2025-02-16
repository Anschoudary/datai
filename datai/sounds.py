import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

# --- Helper Functions ---

def generate_sine_wave(frequency: float = 4.0, duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a sine wave signal.
    """
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * time)
    return time, signal

def generate_cos_wave(frequency: float = 4.0, duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a cosine wave signal.
    """
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.cos(2 * np.pi * frequency * time)
    return time, signal

def generate_square_wave(frequency: float = 4.0, duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a square wave signal.
    """
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * time))
    return time, signal

def generate_sawtooth_wave(frequency: float = 4.0, duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a sawtooth wave signal.
    """
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * (2 * (frequency * time - np.floor(frequency * time + 0.5)))
    return time, signal

def generate_triangle_wave(frequency: float = 4.0, duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a triangle wave signal.
    """
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * (2 * np.abs(2 * (frequency * time - np.floor(frequency * time + 0.5))) - 1)
    return time, signal

def generate_noise(duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a random noise signal.
    """
    signal = amplitude * np.random.uniform(-1, 1, int(sample_rate * duration))
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return time, signal

def generate_chirp_wave(f0: float = 20.0, f1: float = 20000.0, duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a linear chirp signal.
    """
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * f0 * (f1 / f0) ** (time / duration) * time)
    return time, signal

def generate_signal(frequency: float = 4.0, duration: float = 5.0, sample_rate: int = 44100, amplitude: float = 1.0, signal_type: str = 'sine') -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates a signal of a specified type.
    """
    if signal_type == 'sine':
        return generate_sine_wave(frequency, duration, sample_rate, amplitude)
    elif signal_type == 'cosine':
        return generate_cos_wave(frequency, duration, sample_rate, amplitude)
    elif signal_type == 'square':
        return generate_square_wave(frequency, duration, sample_rate, amplitude)
    elif signal_type == 'sawtooth':
        return generate_sawtooth_wave(frequency, duration, sample_rate, amplitude)
    elif signal_type == 'triangle':
        return generate_triangle_wave(frequency, duration, sample_rate, amplitude)
    elif signal_type == 'noise':
        return generate_noise(duration, sample_rate, amplitude)
    elif signal_type == 'chirp':
        return generate_chirp_wave(frequency, duration, sample_rate, amplitude)
    else:
        raise ValueError(f"Invalid signal type: {signal_type}. Please choose from 'sine','cosine', 'square', 'sawtooth', 'triangle', 'noise', or 'chirp'.")

# --- Visualization Functions ---

def visualize_waveform(signal: np.ndarray, sample_rate: int, title: str = "Waveform",
                       file_path: str = None) -> None:
    """
    Visualizes the waveform of a sound signal as a static line plot.

    Args:
        signal (np.ndarray): The sound signal as a NumPy array.
        sample_rate (int): The number of samples per second.
        title (str, optional): The title of the plot. Defaults to "Waveform".
        file_path (str, optional): The path to save the image. If None, the image is not saved.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.
    """

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")

    # Calculate time array directly from signal indices and sample rate
    time = np.arange(len(signal)) / sample_rate

    ax.plot(time, signal, lw=1)  # Plot the entire waveform at once
    ax.set_xlim(0, len(signal) / sample_rate)  # Use signal length for x-axis limit
    ax.set_ylim(signal.min(), signal.max())

    ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            fig.savefig(file_path)
            print(f"Waveform saved to {file_path}")
        except Exception as e:
            print(f"Error saving waveform: {e}. Check file path and permissions.")

def visualize_fft(signal: np.ndarray, sample_rate: int, title: str = "FFT Spectrum",
                  file_path: str = None) -> None:
    """
    Visualizes the frequency spectrum of a sound signal using a Fast Fourier Transform (FFT).
    """

    N = len(signal)
    T = 1 / sample_rate  # Sample spacing
    yf = np.fft.fft(signal)
    xf = np.fft.fftfreq(N, T)[:N//2]

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude")
    ax.plot(xf, np.abs(yf[:N//2]), lw=0.5)  # Plot the entire FFT
    ax.set_xlim(0, sample_rate / 2)
    ax.set_ylim(0, np.max(np.abs(yf[:N//2])) * 1.1)

    ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            fig.savefig(file_path)
            print(f"FFT spectrum saved to {file_path}")
        except Exception as e:
            print(f"Error saving FFT spectrum: {e}. Check file path and permissions.")

def visualize_spectrogram(signal: np.ndarray, sample_rate: int, title: str = "Spectrogram",
                          file_path: str = None,
                          nfft: int = 2048, noverlap: int = 1024) -> None:
    """
    Visualizes the spectrogram of a sound signal with memory-efficient settings.

    Args:
        signal (np.ndarray): The sound signal as a NumPy array.
        sample_rate (int): The number of samples per second.
        title (str, optional): The title of the plot. Defaults to "Spectrogram".
        file_path (str, optional): The path to save the image. If None, the image is not saved.
        datai_label (bool, optional): Whether to add "Datai" label in the bottom right corner. Defaults to True.
        nfft (int, optional): The number of data points used in each block for the FFT. Defaults to 2048.
                              A smaller value reduces memory usage but might decrease frequency resolution.
        noverlap (int, optional): The number of points of overlap between blocks. Defaults to 1024.
                                  A larger value increases computation but can improve feature extraction.
    """
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Frequency (Hz)")

    # Spectrogram with adjusted parameters
    spec = ax.specgram(signal, Fs=sample_rate, cmap='viridis', NFFT=nfft, noverlap=noverlap)
    fig.colorbar(spec[3], ax=ax, label='Intensity (dB)')  # Add a colorbar

    ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            fig.savefig(file_path)
            print(f"Spectrogram saved to {file_path}")
        except Exception as e:
            print(f"Error saving spectrogram: {e}. Check the file path and ensure write permissions.")

def visualize_waveform_fft(signal: np.ndarray, sample_rate: int, title: str = "Waveform and FFT",
                           file_path: str = None) -> None:
    """
    Visualizes the waveform and frequency spectrum of a sound signal side by side.
    """

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot waveform
    time = np.arange(len(signal)) / sample_rate
    ax1.set_title("Waveform and FFT")
    ax1.set_xlabel("Time (s) / Frequency (Hz)")
    ax1.set_ylabel("Amplitude")
    ax1.plot(time, signal, lw=1, label="Waveform")
    ax1.set_xlim(0, len(signal) / sample_rate)
    ax1.set_ylim(signal.min(), signal.max())

    # Create a second y-axis for the FFT
    ax2 = ax1.twinx()
    N = len(signal)
    T = 1 / sample_rate
    yf = np.fft.fft(signal)
    xf = np.fft.fftfreq(N, T)[:N//2]
    ax2.set_ylabel("Magnitude")
    ax2.plot(xf, np.abs(yf[:N//2]), lw=0.5, color='r', label="FFT Spectrum")
    ax2.set_xlim(0, sample_rate / 2)
    ax2.set_ylim(0, np.max(np.abs(yf[:N//2])) * 1.1)

    # Add legends
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    ax1.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax1.transAxes)
    ax2.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax2.transAxes)

    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            fig.savefig(file_path)
            print(f"Waveform and FFT saved to {file_path}")
        except Exception as e:
            print(f"Error saving waveform and FFT: {e}. Check file path and permissions.")

# method for visualizing waveform for two signals for comparison
def visualize_waveform_comparison(signals: list, sample_rate: int, title: str = "Waveform Comparison",
                                  titles: list = None, file_path: str = None) -> None:
    """
    Visualizes the waveform of multiple sound signals for comparison.

    Args:
        signals (list): List of sound signals as NumPy arrays.
        sample_rate (int): The number of samples per second.
        title (str, optional): The title of the plot. Defaults to "Waveform Comparison".
        titles (list, optional): List of titles for each signal. Defaults to None.
        file_path (str, optional): The path to save the image. If None, the image is not saved.
    """

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot each signal with a different color
    colors = plt.cm.viridis(np.linspace(0, 1, len(signals)))
    for i, signal in enumerate(signals):
        time = np.arange(len(signal)) / sample_rate
        label = titles[i] if titles and i < len(titles) else f"Signal {i+1}"
        ax.plot(time, signal, label=label, color=colors[i], lw=1)

    ax.text(0.95, 0.05, "Datai", color='gray', fontsize=8, ha='right', va='bottom', transform=ax.transAxes)

    ax.set_title("Waveform Comparison")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend(loc='upper right') 
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

    if file_path:
        try:
            fig.savefig(file_path)
            print(f"Waveform comparison saved to {file_path}")
        except Exception as e:
            print(f"Error saving waveform comparison: {e}. Check file path and permissions.")

