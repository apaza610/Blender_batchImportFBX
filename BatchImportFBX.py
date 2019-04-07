##################################################################
#   BatchImportFBX (別のcollectionに保存)
#
# For editing Game Assets import a lot of them is needed in FBX but
# keeping them independant from each other is also important
# Author: homar.orozco@gmail.com
# LaPaz-Bolivia
##################################################################

import bpy
import os

def main():
    os.chdir("J:\\borrame\\")   #FBX にある所へ行きます
    Archivos = os.listdir(".")
    for 名前FBX in Archivos:
        crearColeccion(名前FBX)
        bpy.ops.import_scene.fbx(filepath = 名前FBX)

def crearColeccion(名前FBX):
    名前FBX = 名前FBX.replace('.fbx','')
    MiColeccion = bpy.data.collections.new(名前FBX)
    bpy.context.scene.collection.children.link(MiColeccion)
    
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[-1]   #activando ultima coleccion
    
if __name__ == "__main__": main()