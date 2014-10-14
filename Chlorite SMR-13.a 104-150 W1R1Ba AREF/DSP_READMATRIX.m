function returnMatrix = DSP_READMATRIX(fileName)

% =====================================
% to obtain the dimension of the matrix
% =====================================
    % ==========================
    % obtain size in M direction
    % ==========================
    if( exist('Matrix_Size_In_M.check','file') )
        dos('del Matrix_Size_In_M.check');
    end
            % =====================================================================
            % generate a file of M rows, each row contains only 1 value, which is 1
            % i.e. the text file denotes ones(M,1);
            % =====================================================================
            %dos(['for /f "tokens=1,2 delims=<>" %a in (',fileName,') do (echo 1 >> Matrix_Size_In_M.check)']);
            if( exist('DSP_READMATRIX_GETM.bat','file') )
                dos('del DSP_READMATRIX_GETM.bat');
            end
            dos('echo echo off >> DSP_READMATRIX_GETM.bat');    % echo off
            dos(['echo for /f "tokens=1,2 delims=<>" %%a in (',fileName,') do (echo 1 ^>^> Matrix_Size_In_M.check) >> DSP_READMATRIX_GETM.bat']);
            dos('DSP_READMATRIX_GETM.bat');
            dos('del DSP_READMATRIX_GETM.bat');    % to delete the batch
                fid_Matrix_Size_In_M.check = fopen('Matrix_Size_In_M.check');
                fileSizeArray_In_M = fscanf(fid_Matrix_Size_In_M.check,'%f',inf);
                fclose(fid_Matrix_Size_In_M.check);
    dos('del Matrix_Size_In_M.check');

    % =============================================
    % obtain entire matrix in form of column vector
    % =============================================
    if( exist('fileArray_All_As_Column.txt','file') )
        dos('del fileArray_All_As_Column.txt');
    end
    fid_fileArray = fopen(fileName);
    fileArray_All_As_Column = fscanf(fid_fileArray,'%f',inf); % need %f , if %f then error occurs.
    fclose(fid_fileArray);
    DSP_LOG('log matrix to txt','.','fileArray_All_As_Column.txt',fileArray_All_As_Column,' ');
    
    % ===========================================
    % obtain the whole size of the matrix (numel)
    % ===========================================
    if( exist('Matrix_Size_All.check','file') )
        dos('del Matrix_Size_All.check');
    end
            % =====================================================================
            % generate a file of MN rows, each row contains only 1 value, which is 1
            % i.e. the text file denotes ones(M*N,1);
            % =====================================================================
            %dos('for /f "tokens=1,2 delims=<>" %a in (fileArray_All_As_Column.txt) do (echo 1 >> Matrix_Size_All.check)');
            if( exist('DSP_READMATRIX_GETMN.bat','file') )
                dos('del DSP_READMATRIX_GETMN.bat');
            end
            dos('echo echo off >> DSP_READMATRIX_GETMN.bat');    % echo off
            dos('echo for /f "tokens=1,2 delims=<>" %%a in (fileArray_All_As_Column.txt) do (echo 1 ^>^> Matrix_Size_All.check) >> DSP_READMATRIX_GETMN.bat');
            dos('DSP_READMATRIX_GETMN.bat');
            dos('del DSP_READMATRIX_GETMN.bat');    % to delete the batch
            dos('del fileArray_All_As_Column.txt');
                fid_Matrix_Size_All.check = fopen('Matrix_Size_All.check');
                fileSizeArray_All = fscanf(fid_Matrix_Size_All.check,'%f',inf);
                fclose(fid_Matrix_Size_In_M.check);
    dos('del Matrix_Size_All.check');
    % =============================
    % calculate size in N direction
    % =============================
    M  = sum(fileSizeArray_In_M);
    MN = sum(fileSizeArray_All);
    N  = MN / M;

% ======================================================
% generate string '%f %f ... %f' for fscanf use
% the delims is ' ' as default, and there are total N %f
% ======================================================
    % to fasten the string generation
    % magic number of the divider is takens as 8
    runtime = floor( (N-1)/8 );
    remainder = mod( (N-1),8 );
    fscanfString = '%f';
    if( runtime > 0 )
        for i = 1 : runtime
            fscanfString = strcat(fscanfString ,' %f %f %f %f %f %f %f %f');
        end
        for j = 1 : remainder
            fscanfString = strcat(fscanfString ,' %f');
        end
    else
        for i = 1 : N-1
            fscanfString = strcat(fscanfString ,' %f');
        end
    end

% =========
% read file
% =========
fid = fopen( fileName );
returnMatrix = fscanf(fid,fscanfString,[N,M])';     % the transpose is very important
%                                            ^
%                                            |
%               the transpose is very important
fclose(fid);