# sadtalker源码解读
>inference.py

## 
1. 分old_version和new_version
2. 看看模型
   ```
   SadTalker\checkpoints
   ├── SadTalker_V0.0.2_256.safetensors
   ├── SadTalker_V0.0.2_512.safetensors
   ├── mapping_00109-model.pth.tar
   └── mapping_00229-model.pth.tar
   
   SadTalker\gfpgan
   └── weights
       ├── GFPGANv1.4.pth
       ├── alignment_WFLW_4HG.pth
       ├── detection_Resnet50_Final.pth
       ├── parsing_parsenet.pth
       └── tmpamo1u9nq

   SadTalker\src\config
   ├── auido2exp.yaml
   ├── auido2pose.yaml
   ├── facerender.yaml
   ├── facerender_still.yaml
   └── similarity_Lm3D_all.mat
   
   SadTalker\results
   ├── 2023_07_06_19.24.03
   │   ├── first_frame_dir
   │   │   ├── full_body_1.mat
   │   │   ├── full_body_1.png
   │   │   └── full_body_1_landmarks.txt
   │   ├── full_body_1##bus_chinese.mat
   │   ├── full_body_1##bus_chinese.mp4
   │   └── full_body_1##bus_chinese.txt
   └── 2023_07_06_19.24.03.mp4
   ```
1. 从日志看步骤
   - 关键点检测：landmark Det:: 100%|██████████| 1/1 [00:00<00:00, 13.93it/s]
   - 3D人脸重建：3DMM Extraction In Video:: 100%|██████████| 1/1 [00:00<00:00, 50.13it/s]
   - 计算梅尔普：mel:: 100%|██████████| 84/84 [00:00<00:00, 84247.14it/s]
   - 声音转表情：audio2exp:: 100%|██████████| 9/9 [00:00<00:00, 282.00it/s]
   - 人脸渲染：Face Renderer:: 100%|██████████| 42/42 [00:05<00:00,  7.05it/s]
   - 人脸增强：Face Enhancer:: 100%|██████████| 84/84 [00:15<00:00,  5.37it/s]

1. main加载模型
   - sadtalker_paths = init_path：指定很多模型文件：默认256
     - ```
       {
	     'checkpoint': './checkpoints\\SadTalker_V0.0.2_256.safetensors',
	     'dir_of_BFM_fitting': 'F:\\SadTalker\\src/config',
	     'audio2pose_yaml_path': 'F:\\SadTalker\\src/config\\auido2pose.yaml',
         'audio2exp_yaml_path': 'F:\\SadTalker\\src/config\\auido2exp.yaml',
	     'use_safetensor': True,
         'mappingnet_checkpoint': './checkpoints\\mapping_00229-model.pth.tar',
         'facerender_yaml': 'F:\\SadTalker\\src/config\\facerender.yaml'
       }
       ```
   - preprocess_model = CropAndExtract：加载预处理模型
     - 加载关键点检测模型：alignment_WFLW_4HG.pth+detection_Resnet50_Final.pth
     - 加载：resnet50
     - 加载：face_3drecon，从safetensors
     - 加载：similarity_Lm3D_all.mat
   - audio_to_coeff = Audio2Coeff
     - 加载：audio2pose和audio2exp，从safetensors
   - animate_from_coeff = AnimateFromCoeff
     - 加载：facevid2vid，从safetensors
     
1. main运行模型
   - first_coeff_path, crop_pic_path, crop_info =  preprocess_model.generate：预处理
     - 第一步：crop
     - 第二步：关键点检测
     - 第三步：load 3dmm paramter generator from Deep3DFaceRecon_pytorch 
   - ref_eyeblink_coeff_path, _, _ =  preprocess_model.generate
     - 同上预处理
   - ref_pose_coeff_path, _, _ =  preprocess_model.generate
     - 同上预处理
   - batch = get_data(first_coeff_path, audio_path, device, ref_eyeblink_coeff_path, still=args.still)
     - 计算梅尔普+
   - coeff_path = audio_to_coeff.generate
     - 梅尔普转表情，保存到xxx.mat
   - gen_composed_video
     - 跳过先
   - data = get_facerender_data
     - 获取视频
   - result = animate_from_coeff.generate
     - make_animation：渲染视频
     - enhancer_generator_with_len：增强

