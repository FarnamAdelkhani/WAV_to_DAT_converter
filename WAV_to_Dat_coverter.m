%{
   Convert all .WAV input files in a directory to .DAT

Skips opening .WAV meta-data kernel, translates just the signal
values to a simple .DAT file containing the ASCII values.

%}

input_dir = '../WAV_input_files';                 %Input Directory
list_of_files = dir(fullfile(wav_dir, '*.wav'));  %Accumulate list of .wav filelist

for i = 1 : length(list_of_files);   %Iterate all files in directory
    filename = filelist(i).name;

    %Display which file is being worked on
    disp(['Processing ' num2str(i) '/' num2str(length(list_of_files)) ': ' filename])

    %Process each file
    [data, fs] = audioread(fullfile(dir_wav, filename));

    %Save as ASCII .dat file
    save(['../DAT_output_files' filename(1:end-4) '.dat'],'data','-ASCII')

end


%% Use this code if you'd rather specify a single input file
% [data, fs] = audioread('../audioInputs/monoSample.wav');
% save '../audioInputs/monoSample.txt' data -ASCII
